x = 5
y = "5"

#c = x==y
#print(c)
print(x == y)
print( x > int(y))

if(True):
    print("Hello")

if(False):
    print("Hello")

if(False==False):
    print("Hello False")

if(False):
    print("Hello")
elif(True):
    print("true")

if(True):
    print("Hello")
elif(True):
    print("true")

if(False):
    print("Hello")
elif(False):
    print("true")
else:
    print("Apa kabar")

angka = input("Masukan Agka:")
jenis = "ganjil"
if(int(angka)%2==0):
    jenis = "Genap"
print("Angka" + angka + "Tergolong bilangan"+jenis)

massa = int(input("Masukan Massa(kg):"))
tinggi = int(input("Masukan Tinggi(cm):"))

IMT = massa/((tinggi)**2)

text = ""

if(IMT <18.5):
    text = "Berat Badan Kurang"
elif(IMT >= 18.5 and IMT <= 24.9):
    text = "Berat Badan Ideal"
elif(IMT >= 25.0 and IMT <= 29.9):
    text = "BB Berlebih"
elif(IMT >= 30.0 and IMT <= 39.9):
    text = "BB Berlebih"
else:
    text = "Obesitas"
print("Massa"+str(massa)+"kg &tinggi"+ str(tinggi/100)+"m")
print(text)

##Cara lain
a = float(input("Masukan Massa(kg):"))
b = float(input("Masukan Tinggi(m):"))
IMT = (a)/((b)**2)
if(IMT<18.5):
    print("Berat Badan Kurang")
elif(IMT>=18.5 and IMT<24.9):
    print("Berat Badan Ideal")
elif(IMT>=24.9 and IMT<29.9):
    print("Berat Badan Berlebih")
elif(IMT>=29.9 and IMT<39.9):
    print("Berat Badan Sangat Berlebih")
else:
    print("Obesitas")