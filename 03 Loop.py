
#While Loop

angka = 1

while(angka<=11):
    print(angka)
    angka += 1

#For Loop and List
listItem = range(1,11,2)
print(listItem)



########################################Catatan#######################################3
for item in range(5):
    if(item==3):
        break
    print(item)

for item in range(10,0,-1):
    print(item)

listItem = list(range(1,11,2));
print(listItem);
for item in range(1,11,2):
    print(item);

for sans in listItem:
    print(sans)
# 3cara
for item in range(1,11,1):
    print("Nomor Urut:",item);

for item in range(1,11):
    print("Nomor Urut:",item);

for item in range(11):
    if(item > 0):
        print("Nomor Urut:"+ str(item));

for item in range(0,21,2):
    print("kelipatan 2:",item);

listTipe = ["Sans","Gas","Biasa",True,50]
for tipe in listTipe:
    print(tipe)

z='';
for item in range(5):
    z += ' * '
print(z);

z = "*\n*\n*\n*\n*\n"
print(z)

print("\n")
z='';
#mulai dari 0 berakhir 5
for item in range(5):
    for item1 in range(5):
     z += " * "
    z += '\n'
# isi z = *  *  *  *  * \n  *  *  *  *  *\n
print(z);

z='';
for item in range(5):
    for item1 in range(0, item+1):
        z += "*"
    z += '\n'
print(z);


z='';
for item in range(0):
    for item1 in range(5, item-1):
        z -= "*"
    z -= '\n'
print(z);

#solve 1
size = int(input("Masukan Size:"))
z = ""

for num in range(size):
    for num1 in range(num,size):
        z += "*"
        z += "\n"

print(z)

#solve 2

size = int(input("Masukan Size:"))
z = ""

for num in range(size):
    for num1 in range(num,size):
        z += "*"
        z += "\n"
for num in range(size-1):
    for num1 in range(0,num+2):
        z += "*"
    z += "\n"

print(z)


#solve 3
size = size = int(input("Masukan Size:"))
z = ""

for num in range(size):
    for num1 in range(0,size-1-num):
        z += " "
    for num2 in range(0,(num*2)+1):
        z += "*"
    z += "\n"

print(z)

#solve 4

size = size = int(input("Masukan Size:"))
z = ""

for num in range(size):
    for num1 in range(0,num):
        z += " "
    for num2 in range(0,(size*2)-(num*2)-1):
        z += "*"
    z += "\n"

print(z)

#solve 5

size = size = int(input("Masukan Size:"))
z = ""

for num in range(size):
    for num1 in range(0,size-1-num):
        z += " "
    for num2 in range(0,(num*2)+1):
        z += "*"
    z += "\n"

for num in range(size-1):
    for num1 in range(0,num+1):
        z += " "
    for num2 in range(0,((size-1)*2)-(num*2)-1):
        z += "*"
    z += "\n"

print(z)


#angka = 1;
#while(True):
   # print(angka);
   # angka += 1;

angka = 1;
while(False):
    print(angka);
    angka += 1;

#kayak if bedanya if baca sekali while baca terus samapai kondisi false