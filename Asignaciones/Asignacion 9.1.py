fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("The file",fname,"is not valid")
    exit()
semicount = list()
mailbox = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    mail = line.split()
    contact = mail[1]
    semicount.append(contact)
for dir in semicount:
    mailbox[dir] = mailbox.get(dir,0) + 1 
#print(semicount)
#print(mailbox)
maxima_cuenta = None
palabra_max = None
for key,value in mailbox.items():
    if maxima_cuenta is None or value > maxima_cuenta:
        palabra_max = key
        maxima_cuenta = value

print(palabra_max,maxima_cuenta )
