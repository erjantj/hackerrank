def is_palindrome(word):
    word = word.lower()
    len_word = len(word)

    for i in range(len_word//2):
        if not word[i] == word[len_word-i-1]:
            return False

    return True

print(is_palindrome('Deleveled'))
print(is_palindrome('Delevveled'))
print(is_palindrome('Delekveled'))
