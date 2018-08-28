#FizzBuzz

def fizzBuzz(num):
    for i in range(1,num+1):
        if(i%15 == 0):
            print("FizzBuzz")
        elif(i%3 == 0):
            print("Fizz")
        elif(i%5 == 0):
            print("Buzz")
        else:
            print(i)

fizzBuzz(20)

#Fibonacci
def fibo(urut):
    listData = [1,1]
    for i in range(2,urut):
        listData.append(listData[i-2] + listData[i-1])
    return listdata[urut-1]
    #return listdata[-1]

print(fibo(8))

#Reverse List In Place
# bagaimana maksud cara curang?dengan tambahan list baru?
import math

def reverseList(theList):
    for i in range(0,math.floor(len(theList/2)):
        tempList = theList[i]
        theList[i] = theList[len(theList)-1-i]
        theList[len(theList)-1-i] = tempList

    return theList

print(reverseList([1,2,3,4,5,6,7,8]))

#Cara Pakai varable temporaray
import math
def reverse(theList):
    for i in range(math.floor(len(theList)/2)):
        tempList = theList[i]
        theList[i] = theList[len(theList)-1-i]
        theList[len(theList)-1-i] = tempList
    return theList

my_list = [1,2,3,4,5,6,7,8]
print(reverse(my_list))

#Buble Sort

x = [6000,34,203,3,746,200,984,198,764,9,1]

def bubleSort():
    for i in range(len(list),0,1):
        for j in range(0,i-1):
            if(list[j]>list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list
prit(bubleSort(x))

#Mean
x = [1,2,3,2,5,2,7,2]

def getMean(list):
    sum = 0
    for item in list :
        sum = sum + item

    mean = sum / len(list)
    return mean

print(getMean(x))

#Mean cara Lain
x = [5,2,3,2,5,2,7,2]

def Mean(a):
    sum1 = sum(a)
    mean = sum1/len(a)
    return(mean)

print("Mean Cara 1:",Mean(x))

#Mean cara Lain 2
x = [5,2,3,2,5,2,7,2]

def Mean(a):
    return sum(a)/len(a)

print("Mean Cara 2:",Mean(x))

#median
# ada cara sorting cepat
import math
x = [1,2,3,2,5,2,7,2]

def getMedian(list):
    list.sort()
    median = 0
    if (len(list)%2==0):
        median = list[math.floor(len(list)/2)]
    else:
        mid1 = list[int(len(list)/2)-1]
        mid2 = list[int(len(list)/2)]
        median = (mid1+mid2)/2
    return median

print(getMedian(x))

#modus
x = [1,2,3,2,5,2,7,2]

def getMode(list):
    countlist = []
    #create Cont list
    for num in list :
        check = False
        for list1 in countlist:
            if(list[0]==num):
                list = list + 1
                check = True
        if(check == False):
            countlist.append([num,0])

    #create list of ,ode/s
    maxFrequency = 0
    modes = []
    for list in countlist:
        if (list[1] > maxFrequency):
            modes = [list1[0]]
            maxFrequency = list[1]
        elif (list[1] == maxFrequency):
            modes.append(list[0])

    # if every value appears same amount of times

    if(len(modes) == len(countList)) :
        modes = []
    return modes

print(getMode(x))