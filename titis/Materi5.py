# LIST
# list itu kurung kotak [], value bs diubah

# TUPLES
# tuples itu kurang biasa (), value g bs diubah. tp kita bs ngubah value d dalam value di tuples
# contohnya kita ngubah value di dictionary yg ada d dlm tuples

# DICTIONARIES
# dictionaries itu kurung kurawal {}, value bs diubah
# kita spt buat indexing sndr

# LAMBDA
# Function yg g dikasih nama n hanya dipakai sekali

# SET # di dalam set g bs ada list maupun dictionaries. di dalam set bs ada tuples
# tuples bs dimasukin krn nilai tuples g bs diubah
a = {1, 3, 3, 1, 1, 2} # untuk menghilangkan duplicate item

print(a)
print(list(a))

newList = [ 1, (3, "test1"), "test1" , 2, (3, "test1") ]
s = set(newList)
print(s)
print(list(s)[2])
print(list(s))

# LIST COMPREHENSION
listNum = [ 1, 2, 3, 4, 5]
listNum = [item * 2 for item in listNum]
print(listNum)


listNum = [{ "test1" : [5,2]}, {"test1" : [7,3]}]

def test (a,b):
    b =5
    return a+b

listNum = [test(item["test"][1], item["test1"][0]) for item in listNum]
print(listNum)

# MAP
# kelemahannya: cuma bs 1 parameter
listNum = [ 1, 2, 3, 4, 5]
listNum = list(map(lambda num: num * 2, listNum)) # harus pakai function list # setiap elemen di listNum akan dieksekusi sesuia dengan function
print(listNum)

# FILTER
# klw MAP: yang direturn itu akan jd value barunya.
# klw FILTER mengoperasikan function yg mereturn sebuah boolean (True/False), klw False maka data akan dihapus. Status True/False akan menentukan data dihapus atw ngga
# tanpa lambda
def genap(num) : 
    return num % 2 == 0
listNum = [ 1, 2, 3, 4, 5]
listNum = list(filter(genap, listNum))
print(listNum)

listNum1 = [ 1, 2, 3, 4, 5]
listNum1 = list(map(genap, listNum1))
print(listNum1)

# METHODS FOR SEARCHING
numList = [1,2,3]
input = 'x'
check1 = input in numList
check2 = 'x' in ['x','y','z']
check3 = 'ka' in 'kurakas'
print(check1)
print(check2)
print(check3)

# SOAL 1
listData = ["Merdeka", "Hello", "Hellos", "Sohib", "Kari ayam"]
print(listData)
inputUser = input("Search : ")

def searchList(keyWord, theList):
    newList = list(filter(lambda item: keyWord.lower() in item.lower(), theList))
    return newList

searchedList = searchList(inputUser, listData)
print(searchedList)