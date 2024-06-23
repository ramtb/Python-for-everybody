#Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print(fname, "is not a valid file")
    exit()
for line in fh:
    lin = line.rstrip()
    print (lin.upper())