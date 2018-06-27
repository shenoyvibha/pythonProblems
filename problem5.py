#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest():
    for num in range(20000):
        for i in range(21):
            if num%i ==0:
                print(num)
