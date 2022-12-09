def proiz(N):
    a = []
    for i in range(-N,N+1):
        a.append(i)
    return a
N = int(input("Введите число N: "))
string = str(input("Введите 3 индекса через пробел: "))
arr = string.split(' ')

a1 = int(arr[0])
b = int(arr[1])
c = int(arr[2])
a = proiz(N)    
for i in range (len(a)):
    pr = a[a1] * a[b]*a[c]
print (f"Произведение элементов на указанных индексах: {pr}") 