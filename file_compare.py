from sys import argv
from os.path import isfile

if len(argv) == 3:
    files = argv[1:]
else:
    files = []
    for x in ("first", "second"):
        print("Enter %s file name: " % (x), end="")
        files.append(input())

for x in files:
    if not isfile(x):
        print("%s is not a valid file" % (x))
        exit(-1)

match = True

data = []

for x in files:
    with open(x, "rb") as f:
        data.append(f.read())

if data[0] == data[1]:
    print("Files are equal")
else:
    print("Files are different")
