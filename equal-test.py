from sys import stdin


def count_ops(N):
    c = N//5
    N %= 5
    c += N // 2
    N %= 2
    c += N
    return c

assert count_ops(10) == 2
assert count_ops(11) == 3

def solve(N, xs):
    if N == 0:
        return 0
    m = min(xs)
    xs.sort()
    best = 9e99
    for offset in range(6):
        us = [x+offset for x in xs]
        print(us)
        us[0] = xs[0]
        score = sum(count_ops(x-m) for x in us) + count_ops(offset)
        print(offset, [x-m for x in us], [count_ops(x-m) for x in us])
        if score < best:
            best = score
    return best


if __name__ == '__main__':
    assert solve(3,[1,5,5]) == 3
    # assert solve(3,[11,15,20]) == 4
    # T = int(next(stdin))
    # for case in range(T):
    #     N = int(next(stdin))
    #     xs = [int(x) for x in next(stdin).split()]
    #     print(solve(N, xs))