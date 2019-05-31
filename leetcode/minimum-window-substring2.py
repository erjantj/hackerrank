def contains(start, end, t_freqs):
    for c,freq in t_freqs.items():
        if end[c]-start[c] < freq:
            return False

    return True

def minWindow(s, t):
    if not t:
        return ''
    if not s:
        return ''

    s_freqs = {}
    t_freqs = {}
    dp = {0:{}}
    min_len = len(s)
    window = ''

    letters = set()
    for c in t:
        letters.add(c)
        s_freqs[c] = 0
        dp[0][c] = 0
        if not c in t_freqs:
            t_freqs[c] = 0
        t_freqs[c] += 1

    for i in range(len(s)):
        tmp_s_freqs = {}

        if s[i] in s_freqs:
            s_freqs[s[i]] += 1

        for c,freq in s_freqs.items():
            tmp_s_freqs[c] = freq

        dp[i+1] = tmp_s_freqs

    i = 0
    j = 1
    while i < len(s) and j < len(s)+1:
        while not contains(dp[i], dp[j], t_freqs) and j < len(s):
            j += 1

        if not contains(dp[i], dp[j], t_freqs) and i < len(s):
            break

        while contains(dp[i], dp[j], t_freqs) and i < len(s):
            if j-i <= min_len:
                min_len = j-i
                window = s[i:j]
            i += 1

    return window

s = 'adobecodeabanc'
t = 'aabc'

# s = 'ababbaaacbabababaaaaabbb'
# t = 'abbaaaa'

# s = ''
# t = 'abbaaaa'


s = 'ab'
t = 'aa'


print(minWindow(s, t))