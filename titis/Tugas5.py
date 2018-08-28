# # PERCOBAAN 1 MASIH SALAH
# def MainMenu() :
#     inputUser = input("Main Menu : \n 1. Pilih Angka\n 2. Lihat List Angka\n 3. Lihat Score Board\n 4. Keluar\n\n Pilih Menu : ");
#     return inputUser;

# def pilihAngka(inputAngka) :
#     print("Pilihan Angka : ");
#     for i in range(len(inputAngka)) :
#         print(inputAngka[i]);
#     inputUser = input("Mau angka yang mana? : ");
#     return [int(inputUser)]

# def lihatList(inputAngka):
#     print("Ini List Angka : ");
#     for i in range(len(inputAngka)) :
#         print(inputAngka[i]);

# def scoreBoard(inputAngka):
#     print("Score board kita : ")
#     for i in range(len(inputAngka)):
#         if (i == 1):
#             print("benar")
#         else:
#             print ("try again")

# daftarAngka = [1,2,3]
# inputAngka = []

# while True:
#     check = MainMenu();
#     if(check == "1") :
#         inputAngka.append(pilihAngka(daftarAngka));
#     elif(check == "2") :
#         lihatList(inputAngka);
#     elif(check == "3"):
#         scoreBoard(inputAngka)
#     elif(check == "4"):
#         print("Bye!")
#         break


# PERCOBAAN 2 JAWABAN BENAR
lib_lampu={
    '1':["off",1,"off",1,"off"],
    '2':["on",1,"on",2,"on"],
    '3':["on",1,"on",1,"on"],
    '4':["off",3,"on",1,"off"],
    '5':["on",2,"on",1,"on"],
    '6':["on",2,"on",3,"on"],
    '7':["on",0,"on","off"],
    '8':["on",3,"on",3,"on"],
    '9':["on",3,"on",1,"onx"]
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
                if lib_lampu[angka][segment]=="off" : temp+='     '
                elif lib_lampu[angka][segment]=="on" : temp+=' === '
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
