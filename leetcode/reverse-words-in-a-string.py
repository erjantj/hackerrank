def reverseWords(s):
    word_array = s.split()
    s2 = ""
    for i in range(len(word_array)-1, -1 , -1 ):
        s2 += word_array[i]
        if i > 0:
            s2 += " "

    return s2
    
s = "   the       sky is blue         "
s = "   the       "
s = " "
print(reverseWords(s))