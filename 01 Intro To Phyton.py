# Variabel
nama = "Andi"
print("nama:", nama)

usia = 22
usia = 32
print("usia:", usia)

jomblo = True
print("status:", jomblo)

# Data Type
print("\n")
nama = "Yoga"
usia = 22
jomblo = True

print(type(nama))
print(type(usia))
print(type(jomblo))

# Numbers & Arithmetic Operators
print("\n")
usiaAndi = 40
usiaBudi = 20

print("kali: ", usiaAndi * usiaBudi)
print("bagi: ", usiaAndi / usiaBudi)
print("tambah:", usiaAndi + usiaBudi)
print("kurang:", usiaAndi - usiaBudi)
print("modulus:", usiaAndi % usiaBudi)
print("pangkat:", usiaAndi ** 2)

# Numbers & Arithmetic Operators
print("\n")
usiaAndi = 40
usiaBudi = 20

usiaAndi += 3
# usiaAndi = usiaAndi + 3
usiaBudi -= 3
# usiaBudi = usiaBudi - 3

print("usia Andi:", usiaAndi)
print("usia Budi:", usiaBudi)

# Math Module
print("\n")
import math

print("pi:", math.pi)
print("fabs/positif:", math.fabs(-4.7))
print("pow/pangkat :", math.pow(8, 2))
print("sqrt/akar:", math.sqrt(64))

# Round,ceil,floor
print("\n")
print("round:", round(4.6))
print("round:", round(4.4))
print("floor:", math.floor(4.7))
print("ceil:", math.ceil(4.4))

# string
print("\n")
x = "halo dunia hello"

print("len:", len(x))
print("index:", x.index("dunia"))
print("split:", x.split(" "))
print("lower:", x.lower())
print("upper:", x.upper())
print("capitalize:", x.capitalize())

#strings
print("\n")
singleQuetes = 'single quetes'
doubleQuetes = "double quetes"
combinesQuetes = "wrap lot's of other quotes"

print("singlequetes:",singleQuetes)
print("doublequetes:",doubleQuetes)
print("combinesQuetes:",combinesQuetes)

#Strings Indexing
print("\n")
text = "I'm Baron,nice to meet you"

print("indexing 1:",text[1])
print("indexing 2 sampai akhir:",text[2:])
print("indexing 4(4-1) sampai awal :",text[:4])
print("indexing 2 sampai 5(5-1) :",text[2:5])
print("indexing semua :",text[:])

#Adding String & Numbers
print("\n")
usia = 22
nama = "Andi"

print("integer:",usia+usia)
print("string + string:",nama + '  ' + nama)
print("string + integer:",nama + ' ' + str(usia))

#solve it 1
print("\n")
x = 4
y = 3
z = 2

#a = y*z
#b = x+a
#c = x*y
#d = b/c
#e = d**z

w = ((x+y*z)/(x*y))**2

print("hasil:",w)

#solve it 2
#print("\n")
#a = int("silahkan masukan angka berapa pun :")
#hasil = a**2
#print("kuadrat dari " + str(a) + " = " + str(hasil))

#cara lain 1
#print("\n")
#a = input("silahkan masukan angka berapa pun :")
#b = int(a)
#c = b**2
#print(c)

#cara lain 2
#a = input("silahkan masukan angka berapa pun :")

#print(int(a)**2)


#solve it 3
print("\n")
import math
total = 485
tahun = math.floor(total/360)
bulan = math.floor((total%360)/30)
minggu = math.floor(((total%360%30)/7))
hari = math.floor(((total%360)%30)%7)
print(str(total) + "Hari adalah")
print(str(tahun) + "Tahun")
print(str(minggu) + "Minggu")
print(str(hari) + "Hari")

#solve it 4
total = 49
ratiototal = 14
satuan = total/ratiototal

usiaAndi = 4 * satuan
usiaBudi = 10 * satuan
print("Usia Andi 2 tahunlagi = "+str(int(usiaAndi) +2))
print("Usia Budi 2 tahunlagi = "+str(int(usiaBudi) +2))


#solve it 5

x = "Halo Dunia"

print = x.count("a")


#solve it 6
jamAwal = 9
jarak = 120
kecepatanTotal = 100
lama = jarak / kecepatanTotal
print("lama:",lama,"jam")
#cara lain
print("\n")
jarak = 120
kecepatanTotal = 100/3600
lamaDetik = jarak / kecepatanTotal
lamajam = math.floor(lamaDetik/3600)
lamaMenit = math.floor((lamaDetik%3600)/60)

print("lama jam = ",str(lamajam),"lama menit = ",str(lamaMenit))
print("Tabrak Pukul:",str(jamAwal + lamajam),"dan menit ke",str(lamaMenit),"dan detik",str(lamaDetik))




#Convert Strings to Numbers
print("\n")
angka1 = input("masukan angka 1 :")
angka2 = input("masukan angka 2 :")

print("masih dalam string :",angka1 + angka2)
print("berubah jadi integer:",int(angka1)+int(angka2))

angka1 = float(angka1)
angka2 = float(angka2)

print("dalam bentuk float:",angka1+angka2)

print(usia+usia)


# Input
print("\n")
nama = input("What's Your Name: ")
print("nama:", nama)

# solve it
print("\n")
nama = input("nama kamu? : ")
umur = input("umur kamu? : ")
kelamin = input("kelamin kamu? :")
pekerjaan = input("Pekerjaan kamu? : ")

print("nama : ", nama)
print("umur : ", umur)
print("kelamin : ", kelamin)
print("Pekerjaan : ", pekerjaan)
