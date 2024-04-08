n = int(input("Введите натуральное число: "))
if n <= 0:
    print("Введите натуральное число.")
else:
    for i in range(n, 0, -1):
        print(i)
