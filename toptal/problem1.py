def solve(root, values, distinctCount):
    if not root:
        return 0

    if root and root.x not in values:
        distinctCount += 1
        values.append(root.x)

    distinctCountLeft = 0
    distinctCountRight = 0

    if root.l:
        distinctCountLeft = solve(root.l, values, distinctCount)
    if root.r:
        distinctCountRight = solve(root.r, values, distinctCount)

    maxChild = max(distinctCountLeft, distinctCountRight)
    return distinctCount + maxChild


def solution(T):
    if not T:
        return 0

    values = [T.x]
    distinctCountLeft = 0
    if T.l:
        distinctCountLeft = solve(T.l, values, 1)

    values = [T.x]
    distinctCountRight = 0
    if T.l:
        distinctCountRight = solve(T.r, values, 1)

    return max(distinctCountLeft, distinctCountRight)



tree = {
    
}

print(solution(tree))