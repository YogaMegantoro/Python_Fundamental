
# learning "return" function

def total(x,y) : 
    z = x + y 
    return z # fungsi return: ngembaliin ke yang manggil

print(total(4,5))

# learning "recursive" function
def pangkat(x,y):
    if (y == 1):
        return x
    else:
        y -= 1
        return x * pangkat (x,y)

print(pangkat(2,4))

# Default Parameter
def kali(angka1 = 5, angka2 = 2) : 
    return angka1 * angka2
print(kali(angka2=4))

# append in list
buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga']
buah.append('Kelapa')

print(buah) 
buah.pop() 
buah.pop() 
print(buah)

mobil = ["a", "b". "c"]
print(mobil[1:3][1])

x = [1, 3, 2, 6]
x.sort()
print(x)

max = max(x)
min = min(x)

print(max)
print(min)

y = [40, 100, ]




def sortasc(angka):
    asc = []
    while(len(angka)>0):
        terkecil = angka[0]
        for i in range (len(angka)

# sortasc(tugas)

tugas = [40, 100, 1, 5, 25, 10]

def sortasc(list1):
    for i in range(len(list1)):
        for j in range (i+1, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
                print(list1)

# bubble short and selection short
    
sortasc(tugas)

def maxvalue(a):
    max = a[0]
    for num in a:
        if (num > max):
            max = num
    print (max)

maxvalue(tugas)

def minvalue(a):
    min = a[0]
    for num in a:
        if (num < min):
            min = num
    print (min)

minvalue(tugas)