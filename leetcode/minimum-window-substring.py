def minWindow(s, t):
    index = {}
    index_occures = {}
    found_count = 0
    search_count = 0
    start = 0
    end = 0

    s_len = len(s)
    t_len = len(t)

    min_len = s_len
    min_range = (0,0)

    for i in range(t_len):
        index[t[i]] = 0
        index_occures[t[i]] = index_occures.get(t[i], 0)
        index_occures[t[i]] += 1
        search_count += 1   

    for i in range(s_len):
        # add letter
        end = i
        if s[i] in index:
            index[s[i]] += 1
            if found_count < search_count and index[s[i]] <= index_occures[s[i]]:
                found_count += 1

        # reduce
        while found_count >= search_count and start < end:
            if s[start] not in index:
                start += 1
            elif s[start] in index and index[s[start]] > index_occures[s[start]]:
                index[s[start]] -= 1
                if index[s[start]] < index_occures[s[start]]:
                    found_count -= 1
                start += 1
                

            else:
                break
            
        if found_count >= search_count and end-start < min_len:
            min_len = end-start
            min_range = (start, end)

    # reduce
    while found_count >= search_count and start < end:
        if s[end] not in index:
            end -= 1
        elif s[end] in index and index[s[end]] > index_occures[s[end]]:
            index[s[end]] -= 1
            if index[s[start]] < index_occures[s[start]]:
                found_count -= 1
            end -= 1
        else:
            break

    if found_count >= search_count and end-start < min_len:
        min_len = end-start
        min_range = (start, end)

    if found_count >= search_count:
        return s[min_range[0]:min_range[1]+1]

    return ''

s = 'ababbaaacbabababaaaaabbb'
t = 'abbaaaa'
print(minWindow(s, t))