#Problem Statement: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquaresOfFirst100():
    sumOfSquaresOfFirst100 = 0
    for number in range(101):
        sumOfSquaresOfFirst100 = sumOfSquaresOfFirst100 + (number**2)
    return sumOfSquaresOfFirst100

def squareOfSumOfFirst100():
    squareOfSumOfFirst100 = 0
    sumOfFirst100 = 0
    for number in range(101):
        sumOfFirst100 = sumOfFirst100 + number
    squareOfSumOfFirst100 = (sumOfFirst100**2)
    return squareOfSumOfFirst100


sumOfSquaresOfFirst100()
squareOfSumOfFirst100()
result = squareOfSumOfFirst100() - sumOfSquaresOfFirst100()
print(result)