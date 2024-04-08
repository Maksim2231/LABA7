import re

def is_palindrome(s):
    s = re.sub(r'[^\w]', '', s.lower())
    return s == s[::-1]
string = input("Введите строку: ")
if is_palindrome(string):
    print("Введенная строка является палиндромом.")
else:
    print("Введенная строка не является палиндромом.")
