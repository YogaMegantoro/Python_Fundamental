#Function
def contoh():
    print("Halo Dunia")
contoh()

x = 10
y = 5

def contoh():
    print(x+y)
contoh()

#Function with a Parameter
def function(nama):
    print(nama +" Susilo")
function("Andi")
function("Budi")
function("Arda")

#Function with 2 Parameters
#1
def data(x,y):
    print(x,"lahir Tahun",y)

data("Andi","1990")
data("Budi","1991")
data("Caca",1989)
data("tasya",2000)

#2
def total(x,y):
    z = x + y
    return z

print(total(3,9))

#3
z = 0
def total(x, y):
    z = x + y;
    print(z)

print(total(4, 5));
print(z)

#Fn inside Fn

def kali(x):
    if x < 5:
        print(2)
    else:
        return(x*dua())
def dua():
    return(2)

print(kali(6))

#Default Parameter
def kali(angka1 = 5, angka2 = 2) :
    return angka1 * angka2;
print(kali(angka2=4))

#List

#Access List Value
#1
mobil = ["Avansa","Xenia","Ayla"]

print(mobil)
print(mobil[0])
print(mobil[1])
print(mobil[2])
print(mobil[-1])
print(mobil[-2])
print(mobil[-3])

#2
buah = ['Jeruk', 'Nanas', 'Apel'];
for item in buah :
    print(item);

#3
buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga'];
print(buah[1:]);
print(buah[:3]);
print(buah[2:4]);
print(buah[:]);

#Change List Value
buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga'];
buah[1:2:1] = 'Kelapa';
print(buah);

##List append & pop
buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga'];

buah.append("kelapa")
print(buah)
buah.pop()
buah.pop()
print(buah)

#List inside List and Diff Type Data
listTest = [1, 'hi', ['hello', 2, True, [0, 1]]]
print("[1] :",listTest[1]);
print("[:2] :",listTest[:2]);
print("[2] :",listTest[2]);
print("[2][1:] ",listTest[2][1:]);
print("[2][2] :",listTest[2][2]);
print("[2][3][0] :",listTest[2][3][0]);


##########################################################################


#
z = 0
def total(x,y) :
    z = x + y;

print(total(4,5));
print(z)

#
z = 0


def total(x, y):
    z = x + y;
    print(z)


print(total(4, 5));
print(z)


#Recursive Function
def pangkat(x,y):
    if (y==1):
        return x
    else:
        y -= 1
        return x * pangkat(x,y)
print(pangkat(2,4))

# 2*(2*(2*2))


mobil = ["Alya","Xenia","Avanza"]
print(mobil[2])
print(mobil[1:3])
print(mobil[1:3][1])
print(mobil[1:3][:][:][:][0:][:1][0])
mobil[1:] = ["test","karena","cus"]
print(mobil)

def sortAsc(thelist):
    #isisnya dibuat
    print("Say  ")
def sortDsc(thelist):
    # isisnya dibuat
    print("Hello")

x = [40,100,1,5,25,10]
sortAsc(x)
print(x)