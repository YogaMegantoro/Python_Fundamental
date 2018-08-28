print("Selamat datang di Hoki-hoki Bento!")

def printMainMenu():
    inputUser = input("Main Menu : \n 1. Lihat Menu \n 2. Lihat Cart \n 3. Checkout \n 4. Keluar \n\n Pilih Menu :")
    return inputUser

def printMenu(menuList):
    print ("Pilihan Menu : ")
    for i in range (0, len(menuList)): #langsung looping # MenuList terdari dari 0,1,2 # mulai dr 0, lalu 1, lalu 2
        print(str(i+1) + ". " + menuList[i]) # utk menghasilkan 1. ... # akan menghasilkan Pilihan menu yg terdiri dari 3 menu
    inputUser = input("Mau yang mana? : ") # user memasukkan angka bentuk string
    return [int(inputUser)-1, menuList[int(inputUser)-1]]

def printCart(cartList):
    print("Isi Cart : ")
    for i in range (0, len(cartList)):
        print(str(i+1) + ". " + cartList[i][1])

def checkout(cartList, hargaList):
    while True: #unlimited loop
        totalHarga = 0
        print("Item yang dipilih : ")
        for i in range (0, len(cartList)):
            print(str(i+1) + ". " +cartList[i][1])
            totalHarga += hargaList[cartList[i][1]]
        inputDuit = input ("Total Harga Rp " + str(totalHarga) + "\n\n Duit anda berapa? : ")
        if(int(inputDuit) < totalHarga):
            print("Uang anda kurang!")
        else:
            print("Kembaliannya : Rp " + str(int(inputDuit) - totalHarga))
            break

listMenu = ["Paket Bento A Rp 20.000", "Paket Bento B Rp. 25.000", "Paket Bento C Rp 30.000"] # indeks: 0, 1, 2
listHarga = [20000, 25000, 30000]
listCart = []

while True: # unlimited loop sampai user memasukkan input yang benar
    pilihanUser = printMainMenu() #manggil function main menu dan masuk ke "pilihanUser"
    if(pilihanUser == "1"):
        listCart.append(printMenu(listMenu)) # listcart ini kosong dan akan nampung item pilihan user # append: utk masukin data ke list
    elif(pilihanUser == "2"):
        printCart(listCart)
    elif(pilihanUser == "3"):
        checkout(listCart, listHarga)
        listCart = []
    elif(pilihanUser == "4"): # klw kita masukin input 5, akan ngeprint "main menu" lagi
        print("Terima kasih dan sampai jumpa lagi!")
        break # untuk keluar dari looping