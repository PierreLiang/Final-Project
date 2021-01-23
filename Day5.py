#question 12
#500=2*2*5*5*5
#according to the laws of factors, the number of factors is equal to the multiplication of (exponents+1)
#so the smallest number that has 500 roots is 2^(5-1)*3^(5-1)*5^(5-1)*7*11=62370000
#so the lower bound is 62370000
#The basic algorithm is that we will first find the smallest triangle number larger than the
#lower bound which is 6237000, we will create a few functions, one is to test if a number have 500 factors
#this function is basically checking for every number less than the square root of inputted number, if divisible, than the record will plus 1
#also basically the number cound be multiplied by 2 to obtain the number of factors
#two other helper functions are one testing if a number is a triangle number, if it is, we will have another function to find
#the final number that adds up to this triangle number. 
#last, after finding first triangle number bigger than lower bound, we will keep on adding finalnumber+1 to that triangle number
#until a triangle number that has numberoffactors(n) greater than 500
import math
def numberoffactors(n):#function 1, this finds the number of primefactors of a inputted number
    record = 0
    for i in range(1,int(math.sqrt(n))):#the definition of prime factors is that it come up in pairs, one is smaller or equal to the squareroot of the number
    #the other is bigger or equal to the squareroot of the number
        if n%i == 0:
            record += 1#so for each number that is smaller than the squareroot of the number, this means there are 2 factors
    return 2*record
print(numberoffactors(62370000))##quick test to see if function works

def trianglenumber(n):#function 2, determine if this number is a triangle number by squarerooting it and take the integer value, since a triangle number can be expressed as
#a*(a+1)/2, so squareroot of n times (squareroot of n) + 1 divided by 2 would equal n if n is a triangle number
    tn = int(math.sqrt(2*n))
    return tn*(tn+1)/2 == n

print(trianglenumber(15))#quick test to see if function works

def finalnumber(n):#function 3, if a number is a triangle number, find the largest of the list that add up to this number
    if trianglenumber(n):
        return int(math.sqrt(2*n))#the largest of the list is a from the function a*(a+1)/2, a in this case is the integer part of the square root of inputted triangle number

print(finalnumber(15))#quick test to see if function works

lowerbound = 62370000#since from the introduction, we already obtained the smallest number with 500 factors, this means that any number would be at least greater than this
#so 62370000 is the lowerbound

while trianglenumber(lowerbound) == False:
    lowerbound = lowerbound+1#continue adding 1 to the lowerbound to find the first triangle number that is bigger than 62370000
foundanumber=finalnumber(lowerbound)#record the finalnumber of this triangle number so that later, as we determine the upcoming triangle number, we can simply add foundanumber+1 to it

while numberoffactors(lowerbound) < 500 or numberoffactors(lowerbound) == 500:#a loop to stop iterating if the number has more than 500 factors
    lowerbound+=(foundanumber+1)#the lower bound rightnow is the first triangle number bigger than 62370000, each time it will add foundanumber+1 so it will still be a triangle number
    foundanumber=foundanumber+1#foundanumber will also increase by one each time
print(lowerbound)#right now, the lower bound is the triangle number we want that has more than 500 factors. 
#The answer is 76576500
