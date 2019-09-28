class TrieNode(object):
    def __init__(self):
        self.root = {}
        self.wordEnd = False 
        self.word = ''

    def insert(self, word):
        node = self
        for c in word:
            if c not in node.root:
                node.root[c] = TrieNode()
            node = node.root[c]
        node.wordEnd = True
        node.word = word

    def contains(self, letter):
        return letter in self.root

def indexWords(words):
    trie = TrieNode()
    for word in words:
        trie.insert(word)
    return trie

def getNeighbours(board, i, j):
    shifts = [(0,1), (1,0), (0,-1), (-1,0), (-1,1), (1,-1), (1,1), (-1,-1)]
    height = len(board)
    width = len(board[0])
    neightbours = []
    for d in shifts:
        if i+d[0] >= 0 and i+d[0] < height and j+d[1] >= 0 and j+d[1] < width:
            neightbours.append((i+d[0], j+d[1]))
    return neightbours

def dfs(board, node, i, j, visiting, result):
    if (i,j) in visiting:
        return False
    if not node.contains(board[i][j]):
        return False

    visiting.add((i,j))
    node = node.root[board[i][j]]
    if node.wordEnd:
        result.add(node.word)

    neightbours = getNeighbours(board, i,j)
    for neightbour in neightbours:
        isValid = dfs(board, node, neightbour[0], neightbour[1], visiting, result)
    visiting.remove((i,j))
    return True


def boggleBoard(board, words):
    if not board or not words:
        return []

    result = set()
    trie = indexWords(words)
    for i in range(len(board)):
        for j in range(len(board[0])):
            visiting = set()
            dfs(board, trie, i, j, visiting, result)

    return list(result)

words = ['this', 'trumpet', 'is', 'hello', 'order', 'best', 'pies']
board = [
    ['t','h','i','s','t','i'],
    ['r','i','e','l','l','o'],
    ['u','m','p','c','r','a'],
    ['p','r','e','d','b','o']
]

words = ['thir', 'thri']
board = [
    ['t','h'],
    ['r','i'],
]

print(boggleBoard(board, words))