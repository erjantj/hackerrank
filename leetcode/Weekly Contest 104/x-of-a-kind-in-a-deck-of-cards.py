def gcd(a, b):
    if a == 0 : 
        return b  
    return gcd(b%a, a) 

def hasGroupsSizeX(deck):
    if len(deck) < 2:
        return False

    deck = sorted(deck)
    counter = 0
    freqs = set()
    for i in range(1, len(deck)+1):
        counter += 1

        if (i >= len(deck)) or (i < len(deck) and deck[i] != deck[i-1]):
            freqs.add(counter)
            counter = 0

    prevFreq = None
    for f in freqs:
        if f == 1:
            return False
        if not prevFreq:
            prevFreq = f
        else:
            result = gcd(prevFreq, f)
            if result == 1:
                return False

    return True


deck = [1,1]
print(hasGroupsSizeX(deck))
