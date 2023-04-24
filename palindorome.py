def palindrome(word):
    word = word.lower()
    reverse = ""
    for i in word:
        reverse = i + reverse
    if word == reverse:
        return True
    else:
        return False