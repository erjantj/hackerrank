# with open('input.txt') as f:
#     content = f.readlines()

def is_sumilar(s1, s2):
    letters = [False]*28

    s1_len = len(s1)
    s2_len = len(s2)

    for i in range(s1_len):
        letters[ord(s1[i])-97] =True
    for j in range(s2_len):
        if letters[ord(s2[j])-97]:
            return True
    return False


print(is_sumilar('hi', 'world'))