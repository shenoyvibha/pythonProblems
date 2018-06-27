#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
import math


def sumOfPrimes():
    sum = 2
    num = 3
    primeList = [2]
    while(num != 2000000):
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
    print(sum)


sumOfPrimes()