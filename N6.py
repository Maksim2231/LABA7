#Палиндром: Проверьте, является ли введенная пользователем строка палиндромом
#(читается одинаково как слева направо, так и справа налево, игнорируя пробелы, знаки препинания и регистр).


def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Введите текст: ')
if(is_palindrome(something)):
    print('да, это палиндром')
else:
    print ('Это не палиндромчик')