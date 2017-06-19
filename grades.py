#!/usr/bin/env python3

def recgen(known, unknown, toCompute, targetAvg):
    # How many grades haven't been computed yet
    unknownLeft = len(unknown)

    # No more grades to be computed
    if unknownLeft == 0:
        # Get the average grade
        gradeCount = 0
        gradeSum = 0

        for i in range(5):
            gradeCount += known[i]
            gradeSum += known[i] * (i + 1)

        # The average grade is rounded to 2 decimal digits
        gradeAverage = round(gradeSum / gradeCount, 2)

        # Average grade is equal to the one specified by user
        if gradeAverage == targetAvg:
            # Print the computed grades
            print(known)
    # This is the last grade to compute
    elif unknownLeft == 1:
        # Set it to the remaining number of grades to compute
        known[unknown[0]] = toCompute
        recgen(known, unknown[1:], 0, targetAvg)
    else:
        # Test every possible amount the grade could have
        for i in range(toCompute + 1):
            known[unknown[0]] = i
            # Compute the next grade with the remaining number of grades to compute
            recgen(known, unknown[1:], toCompute - i, targetAvg)

def main():
    # Ask the user for the number of pupils who were graded
    print("Pupil count: ", end='')
    pupilCount = int(input())

    # The average grade for the exam
    print("Average grade: ", end='')
    averageGrade = float(input())

    # Array that stores grades that are known for sure
    knownGrades = [None] * 5
    # How many grades are not known
    gradesToCompute = pupilCount
    # Indexes of grades to compute
    unknownGrades = []

    # Ask the user for the number of known grades
    for i in range(5):
        print("Grade " + str(i + 1) + " count (empty if unknown): ", end='')
        strCount = input()

        if not strCount:
            unknownGrades.append(i)
        else:
            knownGrades[i] = int(strCount)
            gradesToCompute -= knownGrades[i]

        del strCount

    # All the grades are known
    if gradesToCompute <= 0:
        print("There are no grades to compute!")
        exit()

    # Run the grade computing algorithm
    recgen(knownGrades, unknownGrades, gradesToCompute, averageGrade)

# Start the main program
main()
