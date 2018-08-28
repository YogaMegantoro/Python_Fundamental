#Cara Accest List
list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
listHasil = [[16,15,14,13],[9,10,11,12],[1,2,3,4],[5,6,7,8]]
list1 = listHasil
print("Baris 0 colom 0:",list1[0][0])
print("Baris 0 colom 1:",list1[0][1])
print("Baris 0 colom 2:",list1[0][2])
print("Baris 0 colom 3:",list1[0][3])
print("Baris 1 colom 0:",list1[1][0])
print("Baris 1 colom 1:",list1[1][1])
print("Baris 1 colom 2:",list1[1][2])
print("Baris 1 colom 3:",list1[1][3])
print(list1)
list1[0][0]=5
print("list1:",list1[0][0])
print("listHasil:",listHasil[0][0])


print("slicing:",list1[0][1:3])