#question 16
a=str(2**1000)
array1=[]
array2=[]
for i in range(0,len(a)):
    array1.append(a[i])
for j in array1:
    array2.append(int(j))
zzz=sum(array2)
print(zzz)
#1366

#question 17

def turnnumber():
    list1=[0,3,3,5,4,4,3,5,5,4.3]#1-10
    list2=[0,6,6,8,8,7,7,9,8,8]#11-19
    list3=[0,6,6,5,5,5,7,6,5]#20-99
    list4=[7,10]#hundred,hundred and 
    n1=sum(list1)+sum(list2)+sum((list3)*10)*10
    n2=list[0]*9+list4[1]*99*9+n1*9
    total=n1+n2+11
    return total
print(turnnumber)
