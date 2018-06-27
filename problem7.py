# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import math

def findPrime():
    sum = 2
    num = 3
    primeList = [2]
    while(len(primeList)!=10001):
        isPrime = True
        for i in primeList:
            if(num % i == 0):
                isPrime = False
                break
            if (i >= math.ceil(math.sqrt(num))):
                    break;
        if(isPrime):
            primeList.append(num)
            sum += num;

        num += 1
    print(primeList)
    length = len(primeList)
    print("The 10001st element is: "+str(primeList[length-1]))

findPrime()