class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def addAsAncestor(self, descendants):
        for descendant in descendants:
            descendant.ancestor = self

def tuneUp(node, depth):
    candidate = node
    while node and depth >= 0:
        candidate = node
        node = node.ancestor
        depth -= 1
    return candidate

def getDepth(node):
    depth = 0
    while node:
        node = node.ancestor
        depth += 1
    return depth
        
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    if not topAncestor:
        return None
    if not descendantOne or not descendantTwo:
        return None
    
    depth1 = getDepth(descendantOne.ancestor)
    depth2 = getDepth(descendantTwo.ancestor)
    
    if depth2 < depth1:
        depth1, depth2 = depth2, depth1
        descendantOne, descendantTwo = descendantTwo, descendantOne

    descendantTwo = tuneUp(descendantTwo, depth2-depth1)    

    while descendantOne.name != descendantTwo.name:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return descendantOne


ancestralTrees = {}
ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for letter in ALPHABET:
    ancestralTrees[letter] = AncestralTree(letter)

ancestralTrees['A'].addAsAncestor([
    ancestralTrees['B'],
    ancestralTrees['C'],
])
ancestralTrees['B'].addAsAncestor([
    ancestralTrees['D'],
    ancestralTrees['E'],
])
ancestralTrees['D'].addAsAncestor([
    ancestralTrees['H'],
    ancestralTrees['I'],
])
ancestralTrees['C'].addAsAncestor([
    ancestralTrees['F'],
    ancestralTrees['G'],
])

print(getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['H'], ancestralTrees['B']).name)
