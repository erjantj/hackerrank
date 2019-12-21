def getNewPattern(pattern):
    if pattern[0] == 'y':
        return ''.join(['y' if c == 'x' else 'x' for c in pattern])
    return pattern

def patternMatcher(pattern, string):
    new_pattern = getNewPattern(pattern)
    
    letters_count = {'x': 0, 'y': 0}
    first_y_pos = 0

    for i in range(len(new_pattern)):
        if new_pattern[i] == 'x':
            letters_count['x'] += 1
        else:
            letters_count['y'] += 1
            if not first_y_pos:
                first_y_pos = i
    

    for x_len in range(1, len(string)):
        x = string[:x_len]
        y = ''
        if letters_count['y'] > 0:
            if (len(string)-x_len*letters_count['x'])%letters_count['y'] != 0:
                continue
            y_len = (len(string)-x_len*letters_count['x'])//letters_count['y']
            y_start_index = x_len*first_y_pos
            if y_start_index+y_len >= len(string):
                continue
            y = string[y_start_index:y_start_index+y_len]

        tmp_string = ''.join([x if c == 'x' else y for c in new_pattern])
        if tmp_string == string:
            return [x,y] if pattern[0] == 'x' else [y,x]
    return []

    
pattern = 'xxyxxy'
string = 'gogorangergogoranger'

pattern = 'yy'
string = ''
print(patternMatcher(pattern, string))

