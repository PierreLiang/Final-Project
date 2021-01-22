#Question 1
#The main idea of solving this problem is to first calculate the multiples of 3 and the multiples of 5. Since the multiple of both 3 and 5 which is 15 is being calculated twice
#We will subtract it from the answer. So number of multiples of 3 and 5=multiples of 3 + multiples of 5 - multiples of 15
count1 = 0 #setting a few variables
count2 = 0
count3 = 0
countof3 = 0
countof5 = 0
countof15 = 0
for i in range (1, 1000):
    if (i % 3 == 0):#calculating how many multiples of threes by seeing how many numbers below 100 is a multiple of 3, similar methods can be applied to 5 and 15
        count1 += 1
    if (i % 5 == 0):
        count2 += 1
    if (i % 15 == 0):
        count3 += 1

countof3=3*(1+count1)*count1*1/2
print(countof3)#easier for debugging
countof5=5*(1+count2)*count2*1/2
print(countof5)
countof15=15*(1+count3)*count3*1/2
print(countof15)
   

totalcount = countof3 + countof5 - countof15#as stated, we can easily calculate the number of multiples of 3 and 5 below 1000 applying the equation above
print(totalcount)
# Answer is 233168


#Question 2

x1=1 #setting up the first 2 numbers as 1,2
x2=2 
x3=-1 #x3 is supposed to be the value of x1 and x2
temp = 0 #this is just a bridge varibable set to transfer the values of x1 and x2
fiblist = []# setting up empty fiblist
totalcount = 0
for i in range (1,100):
    x3 = x1 + x2
    x1 = temp   #swapping and operations that would make 
    temp = x3 #now temp is assign a value which x3 will become the next x2
    x1 = x2
    x2 = temp
    fiblist.append(x3) #x3 is the next number in the list of fibonaci
    x3= -1

#print(fiblist) 
#after inital run, we find out that at the 30th fibonacci number, it is already 3.5 million, the 31st is exceeding the limit.
#So we change the iterations to 30

for j in range (1,31):#since we already observe that there are 31 iterations
    x3 = x1 + x2
    x1 = temp
    temp = x3
    x1 = x2
    x2 = temp
    if (x3 % 2 == 0):#to find all the even numbers
        totalcount += x3 #add it to total count as the sum of even terms
    x3= -1
    print(totalcount+2)#plus the first even number 2
#The Answer is 4613732

#Question 3
#prime factorization is essentially dividing up the number into several primes multiplying each other. Like 30=2*3*5. So the basic algorithm
#is to divide the number inputted with twos first to ensure it is an odd number, then divide every single integer below this number
#if divisible, then the number will be divided and will undergo similar process until it has been primefactorized, then we use max() to find largest prime factor
import math

def primefactorization(n):#this is a more general function where it can take any variables and find the largest prime factor
    factorization=[]
    while n % 2 == 0:#first divide twos from the function so that the number doesn't have any more twos in it, it will be an odd number
        n = n/2
        factorization.append(2)
    for i in range(3, int(math.sqrt(n))):#similar process under go with 3 to the squareroot of this number because it would be repetitive if it is divide every single integer below this numebr)
        while n % i == 0:
            n = n/i
            factorization.append(i)#append the number to the list so that the list will be all the prime factors of the inputted number

    if n > 2:
        factorization.append(n)#the number left after undergoing a bunch of division
    print(factorization)
    print(max(factorization))
n = 600851475143
primefactorization(n)#run the function
#Answer is 6857


