a = ""
listAwal = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
            ]

z = '\n'
for row in range(0, 4):
    for colom in range(0, 4):
        z += '{isi:{fill}{align}{width}}'.format(isi=listAwal[row][colom], fill=' ', align='>', width=4)
        #z+= str(myarray[i][j])
    z += '\n'
print(z)

while a!= 4:
    a int(input)