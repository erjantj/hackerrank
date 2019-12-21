def makePattern(substring):
    patterns = [-1 for i in range(len(substring))]
    i = 1
    j = 0
    while i < len(substring):
        if substring[i] == substring[j]:
            patterns[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = patterns[j-1] + 1
        else:
            i += 1
    return patterns

def doMatch(string, substring, patterns):
    i = 0 
    j = 0

    while i - j + len(substring) <= len(string):
        if string[i] == substring[j]:
            if j == len(substring)-1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = patterns[j-1] + 1
        else:
            i += 1
    return False

def knuthMorrisPrattAlgorithm(string, substring):
    patterns = makePattern(substring)
    return doMatch(string, substring, patterns)

                

string = 'ddabsfgasdsabsfgssfgldssfgldsdsa'
substring = 'absfgssfglds'

# substring = 'aefaedaefaefa'
print(knuthMorrisPrattAlgorithm(string, substring))