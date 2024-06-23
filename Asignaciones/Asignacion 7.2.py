fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("The file:",fname,"is not valid")
    exit()
x=0
y=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        x=x+1
        pos = line.find(":")
        num = line[pos+1:]
        n = float(num)
        y=y+n
        #print(float(num))
print("Average spam confidence:",y/x)
#print(x)    
#print("Done")
