fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("The file",fname,"is not valid")
    exit()
lst = list()
for line in fh:
    sline = line.split()
    for word in sline:
        if not word in lst:
            lst.append(word)
        elif word in lst:
            continue
lst.sort()
print(lst)
