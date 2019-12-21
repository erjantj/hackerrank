class Node:
    def __init__(self):
        self.trie = {}
        self.cache = []

class Solution:
    def suggestedProducts(self, products, searchWord):
        if not products:
            return []
        products.sort()

        if not searchWord:
            return products[:3]

        root = Node()
        for product in products:
            currNode = root
            for letter in product:
                if letter not in currNode.trie:
                    currNode.trie[letter] = Node()
                currNode = currNode.trie[letter]
                currNode.cache.append(product)

        result = []
        currNode = root
        lost = False
        for letter in searchWord:
            if not lost and letter in currNode.trie:
                currNode = currNode.trie[letter]
                result.append(currNode.cache[:3])
            else:
                lost = True
                result.append([])
        
        return result

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

products = ["havana"]
searchWord = "havana"

products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"

products = ["havana"]
searchWord = "tatiana"
print(Solution().suggestedProducts(products, searchWord))