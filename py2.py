def proiz(N):
    pr = 1
    for i in range (1,N+1):
        pr *= i
    return pr
N = int(input("Введите число N: "))
pr = proiz(N)
print(f"Произведение чисел от 1 до {N} равно: {pr}")
