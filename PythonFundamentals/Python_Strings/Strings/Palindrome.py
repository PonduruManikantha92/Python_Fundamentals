def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Optional: normalize by removing spaces and converting to lowercase
    return s == s[::-1]


print(is_palindrome("madam"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("Hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True (with normalization)
