name= input("Enter file: ")
try:
    handle = open(name)
except:
    print("The file",name,"is not valid")
    exit()
cuenta = dict()
for line in handle:
    words = line.split()
    for word in words:
        cuenta[word] = cuenta.get(word,0) + 1

maxima_cuenta = None
palabra_max = None
for key,value in cuenta.items():
    if maxima_cuenta is None or value > maxima_cuenta:
        palabra_max = key
        maxima_cuenta = value

print(palabra_max,maxima_cuenta )
