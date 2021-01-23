#Question 7
#This question asks us to find the 10001 prime number. We need to a thing first-to define what is a prime number. This function is actually useful in later questions
#The idea of defining if a function is prime to divide each number that is less than that number, if all are not divisible, then this number is a prime number
def isprime(n):
    for i in range(2,n):#iterate through every single number below this number
        if n % i == 0:
            return False
    return True#if there are no numbers divisible, than it will return true as it is a prime number.
print(isprime(104743))

def findprime(t):#this function will help us find the nth prime number, we can input any number and it will yield the respective prime number
    primenumber=2#we start at primenumber=2 because we can't include 2 at first so we will start at 2 first
    for i in range(3,t**2,2):#iterate from 3 to t^2 which definitely contain more than 10001 primes
        ini = 1 
        while ini*ini < i:#find the closest value it is to i as a square.
            ini += 2
            if i % ini == 0:
                break
        else:
            primenumber +=1 
            if primenumber == t:
                if isprime(i):#if ths number is a prime number since we iterated 10001 times, than it would be the 10001th prime number
                    return i

print(findprime(10001))#after getting 104743, we will quickly put the number back in the isprime function to test if we got it correct
#The answer is 104743

#Question 8
#for this question we are to find the 13 consecutive numbers that have the largest product. I have found two ways to solve the problem
num = '\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'
recorder=1
numberlist=[]
recordlist=[]
finallist=[]
n=0
for i in range(0,1000):#first append it into a list with each digit is an independent index in the list.
    numberlist.append(number[i])
for j in range(n,n+12):#iterate 13 times in a row, and n start as 0 so the first list is numberlist[0:12], second list is numberlist[1:13]
    recorder=recorder*int(numberlist[j])
    recordlist.append(recorder)
    print(recordlist)#the recorder will record the value for each 13 numbers obtained and we can use max() to know the largest 13 number
    rec=recordlist[-1]
    n+=1
finallist.append(int(rec))
    print(max(finallist))#finally, we obtain this finallist that stores products of each 13 digits in a row

#Silly method
#this is the method that I got my intial answer, it was very tedious
biggest = 0
i = 0
while i < len(num) - 12:# basically I just need to write down every single number and formulate a product of 13 consecutive number, and then each time i will plus 1, 
#this is quite similar to the top it is just the top code has covered the work with a few loops
    one = int(num[i]) #each variable correspond to a digit and since we want 13 consecutive digits, we create thirteen variables
    two = int(num[i+1])  
    thr = int(num[i+2]) 
    fou = int(num[i+3])
    fiv = int(num[i+4])
    six = int(num[i+5])
    seven = int(num[i+6])
    eight = int(num[i+7])
    nine = int(num[i+8])
    ten = int(num[i+9])
    eleven = int(num[i+10])
    twelve = int(num[i+11])
    thirteen = int(num[i+12])

    product = one*two*thr*fou*fiv*six*seven*eight*nine*ten*eleven*twelve*thirteen #and the product can be expressed in this way
    if product > biggest:
        biggest = product#each time there is bigger product, it is replacing the previous to be the biggest, and another one came and make comparison.  
    i = i + 1 
print(biggest)#biggest here will be the largest of all products of 13 consecutive digits.
#Answer is 23514624000

#Question 9
#Pytharagon is defined by a^2+b^2+c^2. Another rule of triangle is that the sum of the length of two sides always exceeds the third side. Since we know the sum is 1000, we 
#can create a function that takes in any sum and try to find any x or y that can formulate pytharagon
def findpytharagon(n):
    for x in range (1,n):#two loops to look for x and y
        for y in range (x+1,x+n+1):
            if(x+y > n):#need to make sure that x+y>n
                break
            z=n-x-y #define z as the 1000-x-y since the sum is 1000
            if(x**2+y**2 == z**2):#the definition of pytharagon numbers an if statement will testify
                print('X is ',x,'Y is ',y)
                return x and y
findpytharagon(1000)
#Answer is X=200, Y=375, Z=425 so XYZ=31875000
