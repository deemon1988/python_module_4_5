def square(x):
    d = x ** 2
    def even(x):
       # d = x * 2
        if d % 2 == 0:
            print("Четное")
        else:
            print("Нечетное")
    even(x)
    return d

a = 5
b = square(5)
print(a)
print(b)