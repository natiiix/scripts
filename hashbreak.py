# This script computes a specified number of MD5 hashes
# that begin with a specified number of leading zeros

import hashlib
import time

# Number of zeros required at the beginning of the computed hash
def const_zeros():
    return 6

# Number of hashes to find for which the condition is satisfied
def const_count():
    return 5

# Determined whether the byte array meets the required condition
def ismagic(byte_array):
    bismagic = True

    # Compute MD5 hash of the byte array
    m = hashlib.md5()
    m.update(byte_array)
    md5_hash = m.hexdigest()

    # Check the number of zeros
    for i in range(const_zeros()):
        if md5_hash[i] != '0':
            bismagic = False
            break

    # Print the hash if it meets the condition
    if bismagic:
        print(md5_hash, end=' - ')
        # Print the byte array for which the condition was met
        for b in byte_array:
            print(str(b).rjust(3), end=' ')
        # Break the line
        print()

    # Return True if the condition was met, False otherwise
    return bismagic

# Main program function
def main():
    counter = 0
    barr = bytearray()

    # Get time at which the computation has started
    starttime = time.time()

    # Until the required number of hashes is computed
    while counter < const_count():
        # Get the current length of the byte array
        barrlen = len(barr)
        # If the byte array is empty or it's full of 255 values
        if barrlen == 0 or barr[barrlen - 1] == 255:
            # Set all the bytes to 0
            for i in range(barrlen):
                barr[i] = 0
            # Add new element to the byte array
            barr.append(0)
        # No need to add another element to the byte array
        else:
            # Increment the lowest byte possible
            for i in range(barrlen):
                # Overflow each element that has value 255
                if barr[i] == 255:
                    barr[i] = 0
                # Increment the lower possible element
                else:
                    barr[i] += 1
                    break

        # If the byte array meets the condition
        if ismagic(barr):
            # Increment the counter of computed hashed that meet the condition
            counter += 1

    # Calculate the time difference between the start of the computation and its end
    totalsec = time.time() - starttime
    # Separate hours, minutes and seconds
    hours = int(totalsec / 3600)
    minutes = int(totalsec / 60 % 60)
    seconds = round(totalsec % 60)

    # Print the computation time
    print("Computation time:", end=' ')

    # Hours
    if hours > 1:
        print(hours, "hours", end=' ')
    elif hours == 1:
        print("1 hour", end=' ')

    # Minutes
    if minutes > 1:
        print(minutes, "minutes", end=' ')
    elif minutes == 1:
        print("1 minute", end=' ')

    # Seconds
    print(seconds, "seconds")

# Start the program
main()
