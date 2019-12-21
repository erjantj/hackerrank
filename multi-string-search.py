class Node(object):
    def __init__(self):
        self.letters = {}
        self.complete = False
        self.index = -1

def indexWord(trie, string, index):
    node = trie
    for c in string:
        if c not in node.letters:
            node.letters[c] = Node()
        node = node.letters[c]
    node.complete = True
    node.index = index

def contains(trie, bigString, i, result):
    node = trie
    curr_index = i
    while node.letters:
        if curr_index >= len(bigString):
            return 
        if bigString[curr_index] not in node.letters:
            return
        if node.complete:
            result[node.index] = True
        node = node.letters[bigString[curr_index]]
        curr_index += 1

    if node.complete:
        result[node.index] = True

def multiStringSearch(bigString, smallStrings):
    trie = Node()
    for i in range(len(smallStrings)):
        indexWord(trie, smallStrings[i], i)

    result = [False for _ in smallStrings]
    for i in range(len(bigString)):
        contains(trie, bigString, i, result)
    return result
    


bigString = 'this is a big string'
smallStrings = ['this', 'yo', 'is', 'a', 'bigger', 'string', 'keppa']

bigString = 'this'
smallStrings = ['this', 'is']

bigString = 'ah samara'
smallStrings = ['sam']


print(multiStringSearch(bigString, smallStrings))

