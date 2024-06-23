check = False
done = "Done"
while check == False:
    fname = input("Enter file name: ") 
    try:
        fh = open(fname)
        check = True
    except:
        if fname == done :
            print("See you soon")
            exit() 
        else:
            print("The file",fname,"is not valid, try again if you don't want to continue, please type Done")
            continue
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    mail = line.split()
    print(mail[1])
    count=count+1
print("There were", count, "lines in the file with From as the first word")
