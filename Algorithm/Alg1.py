def is_palindrome(x):
    return x == (x[::-1])
print(is_palindrome("radar"))
print(is_palindrome("raddr"))