def palindrome(word):
    """
    Using beauty of python
    """
    reverse = word[::-1]
    return word == reverse


print(palindrome('racecar'))
