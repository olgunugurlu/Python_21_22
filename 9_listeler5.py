
#iç içe listeler
a = [1,2,3]#0 1 2 
b = [2,3,4] #0 1 2
c = [4,5,6] #0 1 2
liste1= [a, b, c]
print(liste1)
print(type(liste1))
print(type(liste1[0]))

liste1.append(5)
liste1.append([7,8])
liste1.append('a')
print(liste1)

# liste2 = [[1,2,3],[4,5,6],[7,8,9]]
# print(liste1[0])
print(liste1[2][1])

liste3 = [[[2,3,4],[5,6,7,8]],[[1,2,4],[6,7,8],[8,9,0]]]
print(liste3)