import re
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print(fname, "is not a valid file")
    exit()
count = 0
for line in fh:
    lin = line.rstrip()
    num = re.findall("[0-9]+",line)
    try:
        for n in num:
            inum = int(n)
            count = count + inum
    except:
        continue
print(count)
    