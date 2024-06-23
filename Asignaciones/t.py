largest = None
smallest = None
t = set()
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        snum = int(num)
        t.add(snum)
    except:
        print("Invalid input")
        continue
for fnum in t:
    if smallest is None:
        smallest = fnum
    elif fnum < smallest:
        smallest = fnum
for mnum in t:
    if largest is None:
        largest = mnum
    elif mnum > largest:
        largest = mnum

print("Maximum is", largest)
print("Minimum is", smallest)