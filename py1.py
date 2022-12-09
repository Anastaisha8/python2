def chisl(x):
    s = 0
    for i in  str(x):
        if i != ".":

           s += int(i)
    return s
x = input("Введите вещественное число: ")
s = chisl(x)
print(f"Суммма цифр числа: {s}")

