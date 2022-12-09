def summ(n):
    a = []
    
    for i in range (1,n+1):
        a.append ((1+1/i)**i)
    return sum(a)
n = int(input("Введите число n "))
s = summ(n)
print(f"Сумма последоваельности: {s}")