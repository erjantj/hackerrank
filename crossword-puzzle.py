def parseWord(crossword, point, direction, joints, crosswordMap, openSet, visited):
    directionH = -1
    directionV = 1
    startX = point[0]
    startY = point[1]
    dx = 0
    dy = 0
    length = 0
    knownJoints = set()
    wordJoints = set()

    if direction == directionV:
        dx = 1
    else:
        dy = 1

    xi = point[0]-dx
    yi = point[1]-dy
    while xi >= 0 and yi >= 0 and crossword[xi][yi] == '-':
        visited.add((xi,yi))

        if xi-(1-dx) >= 0 and  yi-(1-dy) >= 0:
            if crossword[xi-(1-dx)][yi-(1-dy)] == '-':
                if (xi,yi) not in joints:
                    wordJoints.add((xi,yi))
                    joints.add((xi,yi))

        if xi+(1-dx) < len(crossword) and yi+(1-dy) < len(crossword[0]):
            if crossword[xi+(1-dx)][yi+(1-dy)] == '-':
                knownJoints.add((xi,yi))
                if (xi,yi) not in joints:
                    wordJoints.add((xi,yi))
                    joints.add((xi,yi))

        length += 1
        startX = xi
        startY = yi

        xi = xi-dx
        yi = yi-dy

    xi = point[0]
    yi = point[1]

    while xi < len(crossword) and yi < len(crossword[0]) and crossword[xi][yi] == '-':
        visited.add((xi,yi))

        if xi-(1-dx) >= 0 and  yi-(1-dy) >= 0:
            if crossword[xi-(1-dx)][yi-(1-dy)] == '-':
                knownJoints.add((xi,yi))
                if (xi,yi) not in joints:
                    wordJoints.add((xi,yi))
                    joints.add((xi,yi))

        if xi+(1-dx) < len(crossword) and yi+(1-dy) < len(crossword[0]):
            if crossword[xi+(1-dx)][yi+(1-dy)] == '-':
                knownJoints.add((xi,yi))
                if (xi,yi) not in joints:
                    wordJoints.add((xi,yi))
                    joints.add((xi,yi))

        xi = xi+dx
        yi = yi+dy
        length += 1

    if (startX, startY, direction) not in openSet:
        openSet.add((startX, startY, direction))
        crosswordMap.append(((startX, startY), direction, length, knownJoints))

    for p in wordJoints:
        parseWord(crossword, p, direction*(-1), joints, crosswordMap, openSet, visited)

def parseBoard(crossword):
    wordCell = '-'
    emptyCell = '+'

    directionH = -1
    directionV = 1

    startX = None
    startY = None
    direction = None

    crosswordMap = [
        # ((x,y), direction, length, {(xi,yi): (xn, yn)})
    ]

    visited = set()

    # search for word cell
    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            if crossword[i][j] == wordCell and (i,j) not in visited:
                startX = i
                startY = j
                if i < len(crossword[i])-1 and crossword[i+1][j] == wordCell:
                    direction = directionV
                else:
                    direction = directionH
                
                parseWord(crossword, (startX, startY), direction, set(), crosswordMap, set(), visited)

    return crosswordMap

def guessFits(guess, guessWordRow, draft):
    xi = guessWordRow[0][0]
    yi = guessWordRow[0][1]
    dx = 0
    dy= 0

    direction = guessWordRow[1]
    if direction == 1:
        dx = 1
    else:
        dy = 1

    for i in range(len(guess)):
        filledCell = draft.get((xi,yi), None)
        if filledCell and filledCell != guess[i]:
            return False
        xi += dx
        yi += dy

    return True

def fillGuess(guess, guessWordRow, draft):
    xi = guessWordRow[0][0]
    yi = guessWordRow[0][1]
    dx = 0
    dy= 0

    direction = guessWordRow[1]
    if direction == 1:
        dx = 1
    else:
        dy = 1

    for i in range(len(guess)):
        draft[(xi,yi)] = guess[i]
        xi += dx
        yi += dy

def clearGuess(guess, guessWordRow, draft):
    xi = guessWordRow[0][0]
    yi = guessWordRow[0][1]
    dx = 0
    dy= 0

    direction = guessWordRow[1]
    if direction == 1:
        dx = 1
    else:
        dy = 1

    for i in range(len(guess)):
        draft[(xi,yi)] = None
        xi += dx
        yi += dy

def solve(crossword, crosswordMap, wordRowIndex, wordsIndex, guess, guesses, draft):
    solved = False

    if guess not in guesses:
        currWordRow = crosswordMap[wordRowIndex]
        joints = currWordRow[3]

        if guessFits(guess, currWordRow, draft):
            fillGuess(guess, currWordRow, draft)
            guesses.add(guess)
            # print(guess, currWordRow, guesses, draft)   
        else:
            return (False, draft)

        # for row in crossword:
        #     print(row)
        # print()

        if wordRowIndex >= len(crosswordMap)-1:
            return (True, draft)
        else:
            nextWordRow = crosswordMap[wordRowIndex+1]
            nextGueses = wordsIndex[nextWordRow[2]]
            # print(guess, nextGueses, guesses)

            for nextGuese in nextGueses:
                solved, draft = solve(crossword, crosswordMap, wordRowIndex+1, wordsIndex, nextGuese, guesses, draft)
                
                if solved:
                    break
            if not solved:
                guesses.remove(guess)
                clearGuess(guess, currWordRow, draft)
            return (solved and True, draft)

    return (False, draft)

def fillCrossword(crossword, draft):
    for point, value in draft.items():
        crossword[point[0]][point[1]] = value
    
def crosswordPuzzle(crossword, words):
    wordsIndex = {}
    
    word = ''
    wordCount = 0
    for char in words:
        if char == ';':
            if not wordCount in wordsIndex:
                wordsIndex[wordCount] = set()
            wordsIndex[wordCount].add(word)

            word = ''
            wordCount = 0
            continue
        word += char
        wordCount += 1
    if not wordCount in wordsIndex:
        wordsIndex[wordCount] = set()
    wordsIndex[wordCount].add(word)

    for i in range(len(crossword)): 
        crossword[i] = list(crossword[i])

    crosswordMap = parseBoard(crossword)
    wordRowIndex = 0
    currWordRow = crosswordMap[wordRowIndex]
    currGueses = wordsIndex[currWordRow[2]]
    
    for guess in currGueses:
        guesses = set()
        solved, draft = solve(crossword, crosswordMap, wordRowIndex, wordsIndex, guess, guesses, {})
        if solved:
            break

    fillCrossword(crossword, draft)
    crosswordResult = []
    
    for row in crossword:
        crosswordString = ''
        for letter in row:
            crosswordString += letter    
        crosswordResult.append(crosswordString)

    return crosswordResult

# crossword = [
# '+-++++++++', 
# '+-++++++++', 
# '+-++++++++', 
# '+-----++++', 
# '+-+++-++++', 
# '+-+++-++++', 
# '+++++-++++', 
# '++------++', 
# '+++++-++++', 
# '+++++-++++'
# ] 
# words = 'LONDON;DELHI;ICELAND;ANKARA'

crossword = [
'++++++++++',
'+------+++',
'+++-++++++',
'+++-++++++',
'+++-----++',
'+++-++-+++',
'++++++-+++',
'++++++-+++',
'++++++-+++',
'++++++++++'
]
words = 'POLAND;LHASA;SPAIN;INDIA'

# crossword = [
# '+-++++++++',
# '+-------++',
# '+-++-+++++',
# '+-------++',
# '+-++-++++-',
# '+-++-++++-',
# '+-++------',
# '+++++++++-',
# '++++++++++',
# '++++++++++'
# ]
# words = 'ANDAMAN;MANIPUR;ICELAND;ALLEPY;YANGON;PUNE'

crossword = [
'+-++++++++',
'+-++-+++++',
'+-------++',
'+-++-+++++',
'+-++-+++++',
'+-++-+++++',
'++++-+++++',
'++++-+++++',
'++++++++++',
'----------'
]
words = 'CALIFORNIA;NIGERIA;CANADA;TELAVIV'

for row in crosswordPuzzle(crossword, words):
    print(row)

