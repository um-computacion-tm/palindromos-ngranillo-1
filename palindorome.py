def palindrome(word):
    word = word.lower()
    reverse = ""
    for i in word:
        reverse = i + reverse
    if word == reverse:
        return True

if palindrome("torot") == True:
    print ("ta 10  ptos capo")
else:
    print ("a laburar capo q esto es una cagada")