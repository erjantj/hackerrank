import string
    
class Solution:
    def find(self, sets, x):
        if x != sets[x]: 
            sets[x] = self.find(sets, sets[x])
        return sets[x]

    def equationsPossible(self, equations):
        sets = {}
        for a, sign, _, b in equations:
            sets[a] = sets.get(a, a)
            sets[b] = sets.get(b, b)

            if sign == "=":
                sets[self.find(sets,a)] = self.find(sets,b)

        for a, sign, _, b in equations:
            if sign == "!" and self.find(sets, a) == self.find(sets, b):
                return False

        return True
                

equations = ["a==b","b!=a"]
equations = ["b==a","a==b"]
equations = ["c==c","b==d","x!=z"]
equations = ["a==b","b!=c","c==a"]
print(Solution().equationsPossible(equations))






