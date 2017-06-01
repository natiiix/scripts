# This script generates a specified amount of prime numbers,
# prints them to screen and displays how long it took to compute them

# This is the second version of the prime number generator
# It is supposed to produce prime numbers faster thanks to an improved algorithm

import time
import math

# Ask the user how many prime numbers do they want to compute
print("Enter the amount of prime numbers to generate: ", end="")
desiredNumCount = int(input())

# Get the time when the computation has started
startTime = time.time()
# Declare the list for storing primes
primeList = []
# 2 is the first number tested for being prime
currNum = 2

# Iterate until the specified number of prime numbers is generated
while len(primeList) < desiredNumCount:
    # Assume that this number is prime
    isPrime = True
    # Testing the remainder after division by higher number than the square root is pointless
    currNumSqrt = int(math.sqrt(currNum)) + 1

    # Test the remainder after division by every number lower than the square root
    for i in range(2, currNumSqrt):
        # If the remainder after division by one of the numbers is 0
        if currNum % i == 0:
            # This number can't possibly be prime
            isPrime = False
            break

    # If the number can't be divided without a remainder, it is a prime number
    if isPrime:
        # Add it to the list of prime numbers
        primeList.append(currNum)

    # Increase the computed prime number counter
    currNum += 1

# The requested amount of prime numbers has been generated
# Get the time when the computation has finished
endTime = time.time()

# Print the calculated primes
print(primeList)

# Print the time spent computing the requested amount of prime numbers
print("Computation time: ", (endTime - startTime), " seconds")
