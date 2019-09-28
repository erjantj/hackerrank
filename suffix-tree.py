# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            node_dict = self.root
            for j in range(i, len(string)):
                if string[j] not in node_dict:
                    node_dict[string[j]] = {}
                node_dict = node_dict[string[j]]
            node_dict[self.endSymbol] = True
            

    def contains(self, string):
        node_dict = self.root
        for c in string:
            if c not in node_dict:
                return False
            node_dict = node_dict[c]

        return self.endSymbol in node_dict

suffixTrie = SuffixTrie('test')
print(suffixTrie.contains('est'))