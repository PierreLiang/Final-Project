#Question 4
#The basic algorithm of this question is to first define what is a palindrome and make it a criteria. Then we can use two iterations to find the two three digit numbers 
#multiplication and find the largest palindrome resulted from the two numbers by finding the maximum of the palindrome list created. 
def palindrome(number):
    return str(number) == str(number)[::-1]#for this I adopted the notation [::-1] which is supposed to reverse the string. I first turn the number into a string and the 
    #basis of palindrome is that it is the same as it is reversed

def find():
    numlist=[]#set up some variables
    a=0
    for i in range(999,100,-1):#since it is three digit numbers, so the upper and lower limits are 999, 100 and since we are looking for the biggest, we need to do it backwards
    #we start at 999 and each iteration we minus 1 instead of starting from 100 and each iteration plus 1
        for j in range(999,100,-1):#a double loop to iterate through the second integer because we are finding two integers
            if palindrome(i*j): #we will get many palindromes as we decrease and this code will return true if the number i times j is a palindrome
                a=i*j
                numlist.append(a)#append each palindrome obtained to a number list, then the maximum of the number list is the palindrome we want to find
    print(max(numlist))
find()
#Answer is 906609

#Question 5
To find the smallest common factor of number below 20. However I created a function that you can input any integer and I can find every single divisible by 
def findprime(n):
    primelist=[]
    for i in range(2,n):
        divide = 0
        for x in range(2,i):
            if i%x == 0:
                divide +=1
        if divide == 0 or i == 2:
            primelist.append(i)
    return primelist
print(findprime(20))
#the system output is [2,3,5,7,11,13,17,19] 

def find(n,t):
    poweroft = 0
    powertlist=[]
    maxnumber = 0
    for i in range(n,0,-1):
        if i % t == 0:
            while i%t == 0:
                i=i/t
                poweroft +=1
            powertlist.append(poweroft)
            poweroft = 0
    return max(powertlist)
ultimatelist=[]
ultimatenumber = 1
prlist=findprime(20)
for i in prlist:
    zzz=find(20,i)
    ultimatelist.append(zzz)
ultimatelist.append(find(20,2))
print(ultimatelist)
prlist.append(2)
print(prlist)
for p in range(0,(len(prlist)-1)):
    ultimatenumber=prlist[p]**ultimatelist[p]
    print(ultimatenumber)
powerofk=0
    powerklist=[]
    for k in range(0,len(prlist)-1):
        for x in range(n,0,-1):
            if x % prlist[k] == 0:
                while x % prlist[k] == 0:
                    x=x/prlist[k]
                    powerofk += 1
                powerklist.append(powerofk)
                print(powerklist)
                powerofk = 0
            allpowers.append(max(powerklist))
    powerklist = []
    allpowers.append(max(power2list))

a=find(20,2)
b=find(20,3)
c=find(20,5)
d=find(20,7)
e=find(20,11)
f=find(20,13)
g=find(20,17)
h=find(20,19)
print((2**a)*(3**b)*(5**c)*(7**d)*(11**e)*(13**f)*(17**g)*(19**h))


