# SOAL 1
def soal1(x,y,z):
    w = ((x + y*z)/(x*y))**z
    return w

jawaban1 = soal1(4,3,2)
print(jawaban1)

# # SOAL 2
angka1 = int(input("Masukkan angka berapapun : "))
print("kuadrat dari " + str(angka1) + " = " + str(angka1**2)

# # SOAL 3
import math
def soal3():
    try:
        total_hari = int(input("Masukkan jumlah hari :"))
        tahun = math.floor(total_hari/360)
        sisa_hari = total_hari%360
        bulan = math.floor(sisa_hari/30)
        sisa_hari1 = sisa_hari%30
        minggu = math.floor (sisa_hari1/7)
        sisa_hari2 = sisa_hari1%7
        hari = math.floor (sisa_hari2)
        print("{} tahun {} bulan {} mingggu {} hari".format(tahun, bulan, minggu, hari))
    except Exception:
        print("Masih error bro!")
soal3()

# SOAL 4
ratioAndi = 2
ratioBudi = 5
ratioTotal = ratioAndi + ratioBudi

umurAndi = 49 * ratioAndi/ratioTotal + 2
umurBudi = 49 * ratioBudi/ratioTotal + 2

print ("Umur Andi: ", umurAndi,
        "\nUmur Budi: ", umurBudi)

# SOAL 5
text = "Halo Dunia"
count_text = text.count("a")
print(count_text)

# SOAL 6
jamAwal = 9
jarak = 120
kecepatanTotal = 100/3600
detikTotal = jarak/kecepatanTotal
lamaJam = math.floor(detikTotal / 3600)
lamaMenit = math.floor((detikTotal%360)/60)
lamaDetik = math.floor((detikTotal%360)%60)
print("Lama jam = " + str(lamaJam) + "Lama menit = " + str(lamaMenit))
print("Tabraknya pukul " + str(jamAwal + lamaJam) + ' dan menit ke ' + str(lamaMenit) + "dan detik ke " + str(lamaDetik))