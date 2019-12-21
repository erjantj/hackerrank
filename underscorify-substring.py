def rangeIntersects(range1, range2):
    if ((range1[0] > range2[1] and range1[1] > range2[1]) or 
        (range1[0] < range2[0] and range1[1] < range2[0])):
        return False
    return True

def underscorifySubstring(string, substring):
    if not string or not substring:
        return string

    ranges = []
    for i in range(len(string)):
        start_index = i
        end_index = i+len(substring)-1
        if string[start_index:end_index+1] == substring:
            tmp_range = (start_index, end_index)
            if ranges and rangeIntersects(ranges[-1], (tmp_range[0]-1, tmp_range[1]+1)):
                ranges[-1] = (min(ranges[-1][0], tmp_range[0]), max(ranges[-1][1], tmp_range[1]))
            else:
                ranges.append(tmp_range)

    range_set = set()
    for r in ranges:
        range_set.add(r[0])
        range_set.add(r[1]+1)

    result = []
    for i in range(len(string)+1):
        if i in range_set:
            result.append('_')
        if i < len(string):
            result.append(string[i])

    return ''.join(result)

string = 'abcacdabcaabcaoabcpabcabcak'
substring = 'abca'
string = 'testetest'
substring = 'test'
print(underscorifySubstring(string, substring))