import numpy as np
list=[]
list1 = []
m = np.random.randint(0,10,(5,5))
#soronként
for i in range(0, m.shape[0]):
    max1 = 0
    for j in range(0, m.shape[1]):
        if m[i, j]>max1 and m[i,j]!=m[j,i]:
            max1=m[i,j]
    list1.append(max1)
list2 = []

#oszlopokként
for i in range(0, m.shape[1]):
    max2 = 0
    for j in range(0, m.shape[0]):
        if m[j, i]>max2 and m[i,j]!=m[j,i]:
            max2=m[j,i]
    list2.append(max2)

print(m)
for i in range(0,5):
    if list1[i]>=list2[i]:
        list.append(list1[i])
    else:
        list.append(list2[i])


print(list)
print("összegük:",sum(list))

