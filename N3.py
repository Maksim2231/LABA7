def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
number = int(input("Введите целое неотрицательное число: "))
if number < 0:
    print("Факториал определен только для неотрицательных чисел.")
else:
    fact = factorial(number)
    print("Факториал числа",number, 'равен', fact)