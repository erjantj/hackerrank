def groupAnagrams(strs):
    freqs = []
    freqs_map = {}

    for w in strs:
        w_map = [0]*26
        for c in w:
            w_map[ord(c)-97] += 1
        w_tuple = tuple(w_map)

        freqs_map[w_tuple] = freqs_map.get(w_tuple, [])
        freqs_map[w_tuple].append(w)

    for key,val in freqs_map.items():
        freqs.append(val)

    return freqs

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
