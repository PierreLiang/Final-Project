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
#To find the smallest common factor of number below 20. However I created a function that you can input any integer and I can find every single divisible by that number 
def findprime(n):#this function tries to find every single prime number that is below the inputted number
    primelist=[]#create an empty list to store values
    for i in range(2,n):
        divide = 0
        for x in range(2,i):#for every number below this number, try to iterate as many iterations as i first, and as i iterate, x iterates with i and divide it from the intial number
            if i%x == 0:
                divide +=1
        if divide == 0 or i == 2:
            primelist.append(i)#if the division is 0 or the only number left is 2, then we can make list of prime numbers 
    return primelist
print(findprime(20))#after initial trial of inputting 20, we get a list of 8 numbers that are primes below 20
#the system output is [2,3,5,7,11,13,17,19] 

def find(n,t):#this function tries to find highest number of times a certain prime number is in a function. n is the upper bound which is 20 in this case, t is the list in prime number  
    poweroft = 0#this serve as a recorder variblae
    powertlist=[]#a recording list
    maxnumber = 0
    for i in range(n,0,-1):#to iterate 20 times in this case
        if i % t == 0:
            while i%t == 0:#find each number that is divisble by the t, which is the inputted prime number obtained from the previous list
                i=i/t
                poweroft +=1
            powertlist.append(poweroft)#append the highest number of times of the occurance of the number into the list. 
            poweroft = 0
    return max(powertlist)
finallist=[] #the final list is a list that has each power corresponding to the prime, list the answer is all the powers multiplied
for j in findprime(20):
    a=find(20,j)
    finallist.append(a)
print(finallist)#just a debugging test
print(2**finallist[0]*3**finallist[1]*5**finallist[2]*7**finallist[3]*11**finallist[4]*13**finallist[5]*17**finallist[6]*19**finallist[7])# the result is primelist*finallist,
#since it is evenly divisible, so need to times 2 to the final result
#Answer is 232792560

#Question 6
#this question is asking us to find the squares of sums as well the sums of square. The sums of square can be solved with a for loop, the square of sums can be applied with the
#formula which denotes the sum from 1 to n=n*(n+1)/2
def sumofsquares(n):
    #this function finds the sum of the squarae using a collector intial number and a for loop
    intialnumber=0
    for i in range(1,n+1):#iterate as many times as the inputted n
        intialnumber += i**2#add the squared value to the collected
    return intialnumber
def squareofsums(n):
    a = (1+n)*n/2 # applying the formula
    return a**2 #then square the result which is the sum
def difference(n):
    return squareofsums(n)-sumofsquares(n)#since we are asked to find the difference, we can simply create another function
print(difference(100))
#The Answer is 25164150

