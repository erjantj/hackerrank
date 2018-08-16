from collections import defaultdict

def solve(queries):
    freqs = defaultdict(int)
    items = defaultdict(int)
    result = []

    for row in queries:
        if row[0] == 1:
            if items[freqs[row[1]]]:
                items[freqs[row[1]]] = items[freqs[row[1]]] - 1
            freqs[row[1]] = freqs[row[1]] + 1
            items[freqs[row[1]]] = items[freqs[row[1]]]+1
        elif row[0] == 2:
            if freqs[row[1]] > 0:
                items[freqs[row[1]]] = items[freqs[row[1]]] - 1
                freqs[row[1]] = freqs[row[1]] - 1
                items[freqs[row[1]]] = items[freqs[row[1]]]+1
        elif row[0] == 3:
            if items[row[1]]>0:
                result.append(1)
            else:
                result.append(0)
    return result

with open('input.txt') as f:
    content = f.readlines()

    n = int(content[0].strip())
    queries = []
    for i in range(1, n+1):
        command, value = [int(x) for x in content[i].strip().split()]
        queries.append((command, value));

    print(solve(queries))