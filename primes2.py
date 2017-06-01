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
    # Get the square root of the currently tested number
    currNumSqrt = int(math.sqrt(currNum))

    # Get the remainder after division by every prime number computer so far
    for i in primeList:
        # Testing the remainder after division by higher number than the square root is pointless
        if i > currNumSqrt:
            break

        # If the remainder after division by one of the prime numbers is 0
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
