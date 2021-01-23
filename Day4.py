#Question 10
#This question is pretty similar to the question I did on day3, again for this question I had two solutions, one is the solution that required so much calculation
#that I still haven't had results from my laptop, the second is an improved algorithm which yielded the correct result
def findprime(n):
#this function's algorithm is straightforward because I failed to taken into account the large calculation that need to be done for this function
    primelist=[]
    for i in range(2,n):
        divide = 0
        for x in range(2,i):#two iterations to find the prime that is less than 2000000
            if i%x == 0:
                divide +=1
        if divide == 0 or i == 2:
            primelist.append(i)#append it to the list of primes
    return primelist
print(findprime(2000000))

#below is the second algorithm and function
import math
def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):#instead of iterating to the whole number, to its square root is enough to prove it is prime, so this is an improvement to the previous is prime function
        if n % i == 0:
            return False
    return True
n=1
sum=0
for i in range(2,2000000):#simply iterating 2000000 is enough in this case
    if isprime(i):
        sum += i #the sum is added to it's previous value
print(sum)
#So for the first algorithm, I estimate the calculation number to be somewhere around 2000000! which is way too big for any laptop in this world
#for the second algorithm, maybe only several trillion calculations, but it is still bearable for my laptop.
#The answer is 142913828922, still even for the second algorithm, it took more than 40 seconds to calculate

#question 13
#this question is particularly interesting, given such a long list of numbers, I thought about using the numpy that we used before for the lab2 biology project
#I went back and found the code to open the file so I first stored the 100 50-digit-numbers into a txt file and use python to open it. 
#Then I created an array and use sum(array) to calculate the sum
import numpy as np
file_name = 'problem13.txt'
with open(file_name,"r") as numbers:#the code to open the txt file
    array1 = []
    for line in numbers:#append each 50 digit number as a seperate object in an array
        array1.append(line)
array2 = []#array 2 is run through array 1 and ensure that every object in the array1 is an integer so we can use the sum() function
for i in array1:
    array2.append(int(i))

findsum=sum(array2)# after finding the sum, we will obtain a really large number and we can turn the number into a string and find the first 10 digits of the string of numbers
print(str(findsum)[:10])#[:10]record the first 10 indexes of the string
#The Answer is 5537376230

#question 15
import math
#This problem involves a lot of math thinking rather than code writing. After first examining this problem, I realized that the basis of this problem is to get from one spot to another
#The final point of the example is 2 units right and down from the initial point. Since each step, you can only take one unit right or down, so this has evolved in a problem of choosing
#In fact, for the example provided, it is essentially 4 steps in total and from the 4 steps, 2 of them should be going right, 2 of them should be going down
#And one have free choice of when to go down or when to go left. So it is basically choosing two steps to be going down out of four steps, then the steps going right are also determined
#So it is basically the combination(4,2)-choosing 2 out of 4 and it should yield 6 which is the correct answer
#So for any a*b grid, it is basically choosing a from a+b which is total of steps that should be taken
#In the case of the question, it is choosing 20 steps to be going down out of a total of 20+20=40 steps so it is C4,2
def C(a,b):#define a function that calculate the paths for any given a*b grid
    x=math.factorial(a)#applying math.factorial as !
    y=math.factorial(b)
    z=math.factorial(a+b)
    combination=z/(x*y)#combination is defined as C(40,20)=40!/(20!)*(40-20)!
    return combination
print(C(20,20))
#The Answer is 137846528820
