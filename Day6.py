#Question 16
#My solution to this problem is too straightforward and involves too much calculation, if it is 2 to the 10000 power or even more, the computer won't be able to handle it,
#however I couldn't think of a better algorithm to approach this problem. So my algorithm is to represent the number 2**1000 as a string first and add them to a list1
#then I will create another list to iterate through list 1 and turn every element to an integer so that I can apply sum() function to find the sum of all digits
def powersof2(n):
    a=str(2**n)#turn 2**1000 to be represented by a string
    array1=[]#create two empty lists to operate with
    array2=[]
    for i in range(0,len(a)):#for each digit element in the string, append it to the list as each individual index
        array1.append(a[i])
    for j in array1:
        array2.append(int(j))#then for each index in the list, iterate through it again and turn it into an integer
    sum=sum(array2)#applying sum() to find the sum of all digits
    return sum
print(powersof2(1000))
#the limitations to this algorithm is that it doesn't accept a number that is too big such as 10000000, because the computer might not be able calculate when the exponent
#is too big, but other then that, the algorithm is fine
#the Answer is 1366

#Question 17
#To solve this question, we need classify the number below 1000 as a few categories
#first category is from one to ten which is recorded in list 1
#second category is 11-19, recorded in list 2
#third category is 20-99, recorded in list 3
#fourth category is "hundred" and "hundred and" recorded in list 4
#remember to add 11 for "one thousand"
def turnnumber():
    list1=[0,3,3,5,4,4,3,5,5,4.3]#1-10
    list2=[0,6,6,8,8,7,7,9,8,8]#11-19
    list3=[0,6,6,5,5,5,7,6,5]#20-99
    list4=[7,10]#hundred,hundred and 
    n1=sum(list1)+sum(list2)+sum((list3)*10)*10#representing numbers from 1-99
    n2=list[0]*9+list4[1]*99*9+n1*9#representing numbers from 100-999
    total=n1+n2+11#all numbers below 1000 can be represented this way
    return total
print(turnnumber)
#There is probably a little problem with code lines 32-33, so I tried fixing and running 5 times but still haven't got the correct answer...

#Question 20
#This question is very similar to question 16, the algorithm is exactly the same, only need to change a bit details to make function work
import math
def factorialsum(n):#receives an input of number to be 'factorialized'
    a=math.factorial(n)#using the math.factorial to quickly find the factorial of a number
    lista=[]
    listb=[]
    b=str(a)
    for i in range(0,len(b)):#same algorithm as q16, lista stores the each digits as an item in the list, but the digits are represented as strings
        lista.append(str(b)[i])
    for j in lista:#the second iteration change each string to digits to make sum() function work
        listb.append(int(j))
    total=sum(listb)
    return total
print(factorialsum(100))
#Again, the factorial of 100 can still be calculated, however, the factorial of say 100000000 can't be calculated with a laptop. So a efficient algorithm is better
#The Answer is 648

