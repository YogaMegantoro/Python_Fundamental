############01Intro to Python#############

#Solve 1
x = 4
y = 3
z = 2

w = ((x/y*z)/(x+y))**2

print("jadi:",w)

#Solve 2
import math

a = int(input("Masukan angka:"))

print("pangkat: ",math.pow(a,2))

#Solve 3
import math
a = 485
tahun = 360
bulan = 30
minggu = 7
hari = 1

tahun = math.floor(a/360)
print(tahun,"tahun")
bulan = math.floor((485%360)/30)
print(bulan,"bulan")
minggu = math.floor(((a%360)%30)/7)
print(minggu,"minggu")
hari = math.floor(((485%360)%30)%7)
print(hari,"Hari")

#Solve 4
totalUsia = 49
totalRasio = 14
usiaAndi = 4*(totalUsia/totalRasio)
usiaBudi = 10*(totalUsia/totalRasio)

UsiaAndi2tahunlagi = usiaAndi+2
UsiaBudi2tahunlagi = usiaBudi+2
print(UsiaAndi2tahunlagi,"Andi")
print(UsiaBudi2tahunlagi,"Budi")

#Solve 5
x = "Halo Dunia"
print("jumlah a",x.count("a"))

#Solve 6
Stotal = 120
A = 60
B = 40
c = A+B
d = Stotal/c
print("Lama",Stotal/c)
print("Waktu Tabrakan",9+d)


#################02-Logic, If, Else If & Else##############

#Solve 1
a = input("Masukan Angka:")
b = "Ganjil"

if (int(a)%2==0):
    b = "Genap"
print(b)

#Solve 2
m = int(input("massa(kg):"))
t = float(input("tinggi(m):"))
IMT = m/(t)**2

if (IMT<18.5):
    print("BB Kurang")
elif(IMT>=18.5 and IMT<=24.9):
    print("BB Ideal")
elif(IMT>24.9 and IMT<=29.9):
    print("BB Berlebih")
elif(IMT>29.9 and IMT<=39.9):
    print("BB Sangat Berlebih")
else:
    print("Obesitas")



#######03-Loop####################

#Solve 1
size = int(input("Masukkan size: "));
z = "";
for num in range(size):
    for num1 in range(num, size):
        z += " * ";
    z += "\n";

print(z);

#Solve 1 Cara lain(Kris)
angka = int(input("Masukan angka:"))
z=""
for A in range(angka,0,-1):
    for B in range(A):
        z = z+"X"
    z = z+"\n"
print(z)

#Solve 2
size = int(input("Masukkan size: "));
z = "";
for A in range(5):
    for B in range(A, 5):
        z += " * ";
    z += "\n";
for A in range(5-1):
     for B in range(0, A+2):
         z += " * ";
     z += "\n";

print(z);

#Solve 2 Cara Lain (Kris.1)
size = int(input("Masukan Angka:"))
baris=''
for i in range(5,1,-1):
    for j in range(0,i):
         baris=baris+'*'
    baris=baris+'\n'
for i in range(1,5+1):
    for j in range(0,i):
        baris=baris+'*'
    baris=baris+'\n'
print(baris)

#Solve 2 Cara Lain (Kris.2)
size = int(input("Masukan Angka:"))
baris=""
for i in range (1,size*2):
    for j in range(0,size+1):
        if j<=abs(i-size):
            baris+='*'
        else:
            baris+=' '
    baris+='\n'
print(baris)

####Cara Yoga Solve 2

z = ""

for row in range(5):
    for colom in range(row,5):
        z=z+"X"
    z= z+"\n"

for row in range(1,5):
    for colom in range(5+row-4):
        z=z+"X"
    z = z+"\n"
print(z)

print(z)


#solve 3
#size=3
z = "";

for A in range(3):
    for B in range(0, 3-1-A):
        z += "   ";
    for C in range(0, (A*2)+1):
        z += " * ";
    z += "\n";

print(z);
#Solve 3 Cara lain kris

baris=''
for A in range(0,5):
    for B in range(1,5*2):
        if B>=5-A and B<=5+A:
            baris=baris+'*'
        elif B<5-A:
            baris=baris+' '
    baris=baris+'\n'
print(baris)

####lebih jelas

baris =""
for row in range(0,5):
    for colom in range(1,5*2):
        if colom>=5-row and colom<=5+row:
            baris=baris+'*'
        elif colom<5-row:
            baris=baris+' '
    baris=baris+'\n'
print(baris)



#solve 4
size = int(input("Masukkan size: "));
z = "";

for num in range(size):
    for num1 in range(0, num):
        z += "   ";
    for num2 in range(0, (size*2)-(num*2)-1):
        z += " * ";
    z += "\n";

print(z)

####cara yoga
z = ""

for row in range(3):
    for spasi in range(row):
        z=z+" "
    for colom in range(0,5-(row*2)):
        z=z+"X"
    z=z+"\n"


print(z)

#Cara Lain Kris
baris=''
for i in range(0,5):
    for j in range(0,5*2-1):
        if j>=i and j<=5*2-2-(i):
            baris=baris+'*'
        elif j<i:
            baris=baris+' '
    baris=baris+'\n'
print(baris)
#solve 5
size = int(input("Masukkan size: "));
z = "";

for num in range(size):
    for num1 in range(0, size-1-num):
        z += "   ";
    for num2 in range(0, (num*2)+1):
        z += " * ";
    z += "\n";
for num in range(1, size):
    for num1 in range(0, num):
        z += "   ";
    for num2 in range(0, (size*2)-(num*2)-1):
        z += " * ";
    z += "\n";

print(z);

##size = 3
z = "";

for row in range(3):
    for spasi in range(0, 3-1-row):
        z += "   ";
    for colom in range(0, (row*2)+1):
        z += " * ";
    z += "\n";
for row in range(1, 3):
    for spasi in range(0, row):
        z += "   ";
    for colom in range(0, (3*2)-(row*2)-1):
        z += " * ";
    z += "\n";

print(z);

#Cara kris

#solve 6

size = int(input("Masukkan size: "));
z = "";

for num in range(size):
    for num1 in range(num, size):
        z += " * ";
    for num2 in range(0, (num*2)-1):
        z += "   ";
    for num3 in range(size, num, -1):
        if(num3 == 1):
           break;
        z += " * ";
    z += "\n";
for num in range(size-1):
    for num1 in range(0, num+2):
        z += " * ";
    for num2 in range(size*2-5, num*2, -1):
        z += "   ";
    for num3 in range(0, num+2):
        if(num == size-2 and num3 == num+1):
           break;
        z += " * ";
    z += "\n";

###Tambahan soal dari yoga
z = ""

for row in range(1,5+1):
    for spasi in range(5-row):
        z = z + " "
    for colom in range(row):
        z = z+"X"
    z = z +"\n"
print(z)


######Bintang ganti saya mau makan(string)#####
z = ""
nama2="Saya Mau Makan Ayam 2 Potong Pakai saus Tiram Bumbu Kecap"

index=0

for row in range(1, 5 + 1):
    for spasi in range(5 - row):
        z = z + " "
    for colom in range(row):
        z = z + nama2[index] #nama2[1]
        index += 1;
    z = z + "\n"
print(z)

#########################################Hoka-Hoki Bento###################

a = ""
listMenu = []
listHarga = []
totalharga = 0
uangUser = 0
while a != 4:
    a = int(input("Main Menu\n1.Lihat Menu\n2.Lihat Cart\n3.Check Out\n4.Keluar\nPilihan Menu:"))

    if (a==1):
        print("1.Paket Bento A Rp 20.000\n2.Paket Bento B Rp 25.000\n3.Paket Bento C Rp 30.000")
        b = int(input("Mau pilih yang mana?:"))
        if(b==1):
            print("Paket bento A Rp20.000")
            listMenu.append("Paket bento A Rp20.000")
            listHarga.append(20000)
        elif(b==2):
            print("Paket Bento B Rp 25.000")
            listMenu.append("Paket Bento B Rp 25.000")
            listHarga.append(25000)
        elif(b==3):
            print("Paket Bento C Rp 30.000")
            listMenu.append("Paket Bento C Rp 30.000")
            listHarga.append(30000)
    print(listMenu)
    print(listHarga)

    if (a==2):
        for item in listMenu:
            print(item)

        for harga in listHarga:
            print(harga)
            totalharga = harga + totalharga
        print(totalharga)

    if (a==3):
        uangUser = int(input("Masukan uang:"))
        if (uangUser<totalharga):
            kurang = abs(uangUser-totalharga)
            print("Uang Anda Kurang: "+str(kurang))
        elif (uangUser==totalharga):
            print("Uang Anda Pas")
            listMenu = []
            listHarga = []
            totalharga = 0

        elif (uangUser>totalharga):
            kembalian = uangUser-totalharga
            print(kembalian,"kembalian")
            listMenu = []
            listHarga = []
            totalharga = 0


####################04-Function & List####################
# Solve 1
def sortAsc(angka):
    asc=[]
    listangka = angka
    while(len(listangka)>0):
        terkecil = listangka[0]
        for i in range(len(listangka)):
            if(listangka[i]<terkecil):
                terkecil = listangka[i]

        listangka.remove(terkecil)
        asc.append(terkecil)
    return asc

x = [40,100,1.5,25,10]
print(sortAsc(x))

#Sort
def sort(theList,fn):
    for i in range(len(theList)):
        for j in range (i+1,len(theList))
            check = fn(theList(i)), theList(j)
            if(check>0):
                temp = theList(i)
                theList(i) = theList(j)
                theList(j) = temp

#Max

def minMax(theList):
    min = theList[0]
    max = theList[0]
    for i range(1,len(theList)):
        if(min>theList[i]):
            min = theList

###########Yoga
solve 1
tugas = [40, 100, 1.5, 25, 10]
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
                print(list1)
sortasc(tugas)
#### with function
a = [40,100,1,5,25,10]

def sort(tugas):
    for i in range (len(tugas)):
        for j in range (i+1,len(tugas)):
            if(tugas[i]>tugas[j]):
                tugas[i] , tugas[j] = tugas[j] , tugas[i]
    return tugas

print(sort(a))
###solve 2
tugas = [40,100,1,5,25,200]

min = tugas[0]
for num in tugas:

    if (num < min):
        min = num
print(min)

##function
a = [40,100,1,5,25,10]
def max (tugas):
    max = tugas[0]
    for b in tugas:
        if(b>max):
            max=b
    return max

print(max(a)

###############05-Lambda Exp, Tuples & etc####################
# Cara kris
mylist = ["Merdeka","Hello","Hellos","Sohib","Kari Ayam"]
listhasil = list(filter(lambda kata:"ka" in kata.lower(),mylist))
print(listhasil);

#purwadika
listdata = ["Merdeka","Hello","Hellos","Sohib","Kari Ayam"]
print(listdata)
inputuser = input("search:")

def searchlist(keyWord,thelist):
    newList = list(filter(lambda item: keyWord.lower() in item.lower(),thelist))
    return newList

searchedlist = searchlist(inputuser,listdata)
print(searchedlist)

###########
Main Menu
1.Lihat semua Dictionary
2.Tambahkan New Dictionary
3.Filter isi Dictionary
4.keluar

input key : maruka
1.number
2.string
masukan 2
input value kerasakti

a = ""
key = {}
dictionary = {}
inputvalue = {}

while a!= 4:
    a = int(input("Main Menu\n1.Lihat Full Dictionary\n2.Isi Dictionar\n3.Searching Dictionary\n4.Keluar\n\nPilih:"))
    if(a==1):
        print("Isi Full Dictionary")
        print("___________________________________________________")
        print("|     Key            |       Value                |")
        for key in dictionary:
            if(type(dictionary[key])==str):
                print("|_____"+key+"________|________"+dictionary[key]+"______|")
            elif(type(dictionary[key])==int):
                print("|_____"+key+"________|________"+str(dictionary[key])+"______|")
    if(a==2):
        key = input("Isi Key:")

        jenisvalue = int(input("Pilih 1 Untuk String Pilih 2 Untuk Number:"))
        if(jenisvalue==1):
            inputvalue = str(input("value:"))
            dictionary[key]= inputvalue
            print(dictionary)


        elif(jenisvalue==2):
            inputvalue = int(input("value:"))
            dictionary[key]=inputvalue
            print(dictionary)

    if(a==3):
        masukan = input("search:")
        listhasil = list(filter(lambda kata: masukan in kata.lower(), dictionary))
        print(listhasil);

    if(a==4):
        a = ""
        key = {}
        dictionary = {}
        inputvalue = {}

#############7Segmen

lib_lampu={
    '1':[0,1,0,1,0],
    '2':[1,1,1,2,1],
    '3':[1,1,1,1,1],
    '4':[0,3,1,1,0],
    '5':[1,2,1,1,1],
    '6':[1,2,1,3,1],
    '7':[1,1,0,1,0],
    '8':[1,3,1,3,1],
    '9':[1,3,1,1,1]
}

def MainMenu() :
    inputUser = input("Main Menu : \n 1. Input List\n 2. Lihat List\n 3. Keluar\n\n Pilih Menu : ");
    return inputUser;
print(lib_lampu)

def lihatList(inputAngka):
    temp=''
    for segment in range(0,5):
        for angka in inputAngka:
            if segment==0 or segment==2 or segment==4:
                if lib_lampu[angka][segment]==0 : temp+='     '
                elif lib_lampu[angka][segment]==1 : temp+=' === '
            elif segment == 1 or segment == 3:
                if lib_lampu[angka][segment]==0 :   temp+='     '
                elif lib_lampu[angka][segment]==1 : temp+='    |'
                elif lib_lampu[angka][segment]==2 : temp+='|    '
                elif lib_lampu[angka][segment]==3 : temp+='|   |'
            temp+='   '
        temp+='\n'
    print(temp)
    print(inputAngka)

inputAngka = []
while True:
    check = MainMenu();
    if(check == "1") :
        inputAngka.append(input('Masukkan Angka(1-9): '))
    elif(check == "2") :
        lihatList(inputAngka);
    elif(check == "3"):
        print("Bye!")
        break

#########################
lib_lampu={
    '1':[0,1,0,1,0],
    '2':[1,1,1,2,1],
    '3':[1,1,1,1,1],
    '4':[0,3,1,1,0],
    '5':[1,2,1,1,1],
    '6':[1,2,1,3,1],
    '7':[1,1,0,1,0],
    '8':[1,3,1,3,1],
    '9':[1,3,1,1,1],
    "0":[1,3,0,3,1]
}
z = ""
a = ""
b = []
while a != 3:
    a = int(input("Main Menu\n1.Input Menu\n2.List Menu\n3.Keluar\n\nPilih Menu: "))
    if(a==1):
        b.append(str(input("Masukan Angka")))
        for segmen in range(0,5):
            for angka in b:
                if segmen==0 or segmen==2 or segmen==4:
                    if lib_lampu[angka][segmen]==0:
                        z = z+ "     "
                    elif lib_lampu[angka][segmen]==1:
                        z = z+" === "
                elif segmen==1 or segmen==3:
                    if lib_lampu[angka][segmen]==0:
                        z = z+"     "
                    elif lib_lampu[angka][segmen]==1:
                        z = z+"    |"
                    elif lib_lampu[angka][segmen] == 2:
                        z = z+"|    "
                    elif lib_lampu[angka][segmen] == 3:
                        z = z+"|   |"
                z = z+"     "
            z=z+"\n"
        print(z)
    if(a==2):
        print(z)
    if(a==3):
        z = ""
        a = ""
        b = []

#############
buatlah list 2 dimensi(list dalam list)berukuran 4X4 bisa diputar kekanan atau kekiri tergantung user dan diputar berapa
kali tergantung user juga


a = ""
listAwal = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]

z = '\n'
for row in range(0, 4):
    for colom in range(0, 4):
        z += '{isi:{fill}{align}{width}}'.format(isi=listAwal[row][colom], fill=' ', align='>', width=4)
        #z+= str(myarray[i][j])
    z += '\n'
print(z)

while a !=0:
    a = int(input("1.Puter kanan\n2.Puter Kiri\n3.Keluar\nPilih:"))
    if(a==1):
        jumlahMuter = int(input("Mau Diputar Kanan Berapa Kali:"))
        #z = [[0 for colom in range(0,4)] for row in range(0,4)]
        listHasil = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]

        for muterKali in range(jumlahMuter):
            for row in range(0,4):
                for colom in range(0,4):
                    listHasil[colom][abs(row-3)] = listAwal[row][colom]

            listAwal = list(listHasil)
            listHasil = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]


        b = '\n'
        for row in range(0, 4):
            for colom in range(0, 4):
                b += '{isi:{fill}{align}{width}}'.format(isi=listAwal[row][colom], fill=' ', align='>', width=4)
                # z+= str(myarray[i][j])
            b += '\n'
        print(b)

    if (a == 2):
        jumlahMuter = int(input("Mau Diputar Kiri Berapa Kali:"))
        # z = [[0 for colom in range(0,4)] for row in range(0,4)]
        listHasil = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]

        for muterKali in range(jumlahMuter):
            for row in range(0, 4):
                for colom in range(0, 4):
                    listHasil[abs(colom-3)][(row)] = listAwal[row][colom]

            listAwal = list(listHasil)
            listHasil = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        b = '\n'
        for row in range(0, 4):
            for colom in range(0, 4):
                b += '{isi:{fill}{align}{width}}'.format(isi=listAwal[row][colom], fill=' ', align='>', width=4)
                # z+= str(myarray[i][j])
            b += '\n'
        print(b)


