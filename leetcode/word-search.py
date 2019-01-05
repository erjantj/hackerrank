def helper(board, word, letter_index, visited, pos, depth = 0):
    if depth >= len(word):
        return True
    if visited.get(pos, False):
        return False
    if word[depth] != board[pos[0]][pos[1]]:
        return False

    visited[pos] = True
    print(board[pos[0]][pos[1]], pos)

    result1 = False
    result2 = False
    result3 = False
    result4 = False

    if pos[0]-1 >= 0:
        result1 = helper(board, word, letter_index, visited, (pos[0]-1, pos[1]), depth + 1)
    if pos[1]-1 >= 0:
        result2 = helper(board, word, letter_index, visited, (pos[0], pos[1]-1), depth + 1)
    if pos[0]+1 < len(board):
        result3 = helper(board, word, letter_index, visited, (pos[0]+1, pos[1]), depth + 1)
    if pos[1]+1 < len(board[0]):
        result4 = helper(board, word, letter_index, visited, (pos[0], pos[1]+1), depth + 1)

    result = result1 or result2 or result3 or result4

    if not result:
        visited[pos] = False
        
    return result

    
def exist(board, word):
    if not word:
        return True
    if not board:
        return False

    letter_index = {}

    for i in range(len(board)):
        for j in range(len(board[i])):
            letter = board[i][j]
            letter_index[letter] = letter_index.get(letter, [])
            letter_index[letter].append((i,j))

    if word[0] not in letter_index:
        return False

    if len(word) == 1:
        return True

    result = False
    for pos in letter_index[word[0]]:
        visited = {}
        if result:
            break
        result = result or helper(board, word, letter_index, visited, pos)

    return result

board = [
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
]

# word = "ABCCED"
# # return true.
# word = "SEE" 
# # return true.
# word = "ABCB"
# # return false.
word = "ABCESEEEFS"

print(exist(board, word))
