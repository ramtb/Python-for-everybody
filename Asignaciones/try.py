fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("The file",fname,"is not valid")
    exit()
semicount = list()
hours = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    mail = line.split()
    time = mail[5]
    clock = time.split(":")
    hour = clock[0]
    semicount.append(hour)
for dir in semicount:
    hours[dir] = hours.get(dir,0) + 1 
#print(semicount)
#print(hours)
ihours = sorted(hours.items())  
top5 = list()
for k,v in ihours:
    invh = (v,k)
    top5.append(invh)
top5 = sorted(top5,reverse=True)
print("Top 5 of hours of recieving an email")
for v,k in top5[:6]:
    print(k,v)