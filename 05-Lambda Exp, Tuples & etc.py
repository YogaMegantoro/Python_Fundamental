#Pelajari
tesList  = [1,2,3]
newList = tesList.copy()

newList[2] = "test"

print(tesList)
print(newList)

#Pelajari membedakan ketiban dan tidak



#Dictionaries
d = {"key1":"item1","key2":"item2","kucing":[3,"jerapah"]}

print(d["key1"])
print(d["key2"])
print(d["kucing"])
print(d["kucing"][1])

#Dictionaries inside Dictionaries
a = {"key1":{"key2":"item2"},"kucing":[3,"jerapah"]}

print(a["key1"])
print(a["key1"]["key2"])
print(a["kucing"])
print(a["kucing"][1])

#Penuisan dictionary
a = "test"
b = 20
d = {""+a+"": 5,str(b):10}
print(d)

d = {"test1":"test","test2":10}
print(d)

#Penulisan dictionary
a = "test"
b = 20
d = {""+a+"": 5,str(b)+"":10,"maruk":[7,8]}

for item in d:
    print(item)
for item in d:
    print(d[item])

d["keren"] = 70
print(d)



#Tuples
t = (1,[0,"test"],{"a1":True})

print(t[2]["a1"])
print(t[1][1])
t[1][1] = "akan"
print(t[1][1])
t[1] = "mark"
print(t[1])

#Tuples inside Tuples
t = (1, [0, "test"], { "a1" : True }, (0,{ "test" : 5 },2));
print(t[3][1]["test"]);

#Sets
s = { 1, 3, 1, 2, 2, 3 };
print(s);
print(list(s)[2]);

#Filtering List using Set
newList = [ 1, 3, "test1", "test2" , 2, 3, "test1" ];
s = set(newList);

print("s:",s);
print(list(s)[2]);

#List Comprehension
#Cara Lama
listNum = [ 1, 2, 3, 4, 5];
for i in range(len(listNum)):
    listNum[i] *= 3
print(listNum)
#1
listNum = [ 1, 2, 3, 4, 5];
listNum = [item * 2 for item in listNum];
print(listNum);

#2
def times2(num) :
    return num * 2;
listNum = [ 1, 2, 3, 4, 5];
listNum = [times2(item) for item in listNum];
print(listNum);

####Pelajari
listNum = [{"test1" : [5,2]},{"test1" :[7,3]},{"test1" :[9,7]}]
def test(a,b):
    b = 5
    return a+b

listNum = [test(item["test1"][1],item["test1"][0]) for item in listNum]
print(listNum)

#Lambda  Expressions

def times2(num) :
    return num * 2;

lambda num: num * 2;

#MAP
#1 MAP without lambda
def times2(num) :
    return num * 2;
listNum = [ 1, 2, 3, 4, 5];
listNum = list(map(times2, listNum));
print("without lambda:",listNum);

#2 MAP lambda
listNum = [ 1, 2, 3, 4, 5];
listNum = list(map(lambda num: num * 2, listNum));
print("with lambda:",listNum);

#Filter
#Without Lambda (using function) :
def genap(num) :
    return num % 2 == 0;
listNum = [ 1, 2, 3, 4, 5];
listNum = list(filter(genap, listNum));
print(listNum);

#With Lambda :
listNum = [ 1, 2, 3, 4, 5];
listNum = list(filter(lambda num: num % 2 == 0, listNum));
print(listNum);

####Pelajari
def genap(num) :
    return num % 2 == 0;

listNum = [ 1, 2, 3, 4, 5];
listNum = list(map(genap, listNum));
print(listNum);

def genap(num) :
    return True

listNum = [ 1, 2, 3, 4, 5];
listNum = list(filter(genap, listNum));
print(listNum);

def genap(num) :
    return num % 2 == 0;

listNum = [ 1, 2, 3, 4, 5];
listNum = list(map(genap, listNum));
print(listNum);

def genap(num) :
    return False

listNum = [ 1, 2, 3, 4, 5];
listNum = list(filter(genap, listNum));
print(listNum);



#Methods for Searching
numList = [1,2,3];
input = 'x';
check1 = input in numList;
check2 = 'y' in ['x','y','z'];
check3 = 'ka' in 'kurakas';
print("check1:",check1);
print("check2:",check2);
print("check3:",check3);

#Solve
mylist = ["Merdeka","Hello","Hellos","Sohib","Kari Ayam"]
listhasil = list(filter(lambda kata:"ka" in kata.lower(),mylist))
print(listhasil);
