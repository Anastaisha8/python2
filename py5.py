import random 
def spisok(sp):
    random.shuffle(sp)
    return sp
sp = list(map(str,input("Введите элементы списка: ")))
sp = spisok(sp)
print(f"Перемещанный список: {sp}")
