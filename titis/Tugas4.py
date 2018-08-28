x = [40, 100, 1, 5, 25, 10]

def sort(thelist, fn): # kita bs kirim function ke function ln sbg parameter
    for i in range (len(thelist)):
        for j in range(i+1, len(thelist)):
            check = fn(thelist[i], thelist[j])
            if(check > 0):
                temp = thelist[i]
                thelist[i] = thelist[j]
                thelist[j] = temp
    
def minmax(thelist):
    min = thelist[0] # kita jadikan acuan dulu krn belum ada perbandingan
    max = thelist[0]
    for i in range(1, len(thelist)):
        if(min > thelist[i]):
            min = thelist[i]
        if(max < thelist[i]):
            max = thelist[i]

    return[min, max]

sort (x, lambda a,b: a-b) # lambda g bs multiple line, function 1 line aja
print(x)
sort(x, lambda a,b: b-a)
print(x)