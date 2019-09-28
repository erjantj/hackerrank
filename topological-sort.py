def ts(g, visited, gray_set, stack, job):
    if job in gray_set:
        return False

    if job in visited:
        return True

    gray_set.add(job)
    visited.add(job)
        
    result = True
    for child in g[job]:
        result = result and ts(g, visited, gray_set, stack, child)
    stack.append(job)
    gray_set.remove(job)

    return result

def topologicalSort(jobs, deps):
    g = {}
    for j in jobs:
        g[j] = []
    
    for j1, j2 in deps:
        g[j1].append(j2)        
    
    stack = []
    visited = set()
    gray_set = set()
    result = True
    for j in jobs:
        if j not in visited:
            result = result and ts(g, visited, gray_set, stack, j)
    if not result:
        return []
    return list(reversed(stack))

jobs = [1,2,3,4,5]
# deps = [[1,2],[1,3],[3,2],[4,2],[4,3]]
deps = [[1,2],[2,3],[3,4]]
print(topologicalSort(jobs, deps))



#      1
# 4 \ / \
#  \ /_ 3
#   2 /
