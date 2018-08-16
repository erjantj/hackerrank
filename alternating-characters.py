def alternatingCharacters(s):
    prev = None
    deletions = 0
    for i in s:
        if i == prev:
            deletions += 1
        prev = i

    return deletions

with open('input.txt') as f:
    content = f.readlines()
    n = int(content[0])
    for i in range(1, n+1):
        s = content[i].strip()
        print(alternatingCharacters(s))
