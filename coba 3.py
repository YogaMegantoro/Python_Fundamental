
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
