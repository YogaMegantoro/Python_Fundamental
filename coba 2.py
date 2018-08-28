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
