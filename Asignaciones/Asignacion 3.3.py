grade = input("Enter score: ")
try:
    gr = float(grade)
except:
    print("Error, enter a numeric input")
    quit()
if gr >= 0.9:
    print("A")
elif gr >= 0.8:
    print("B")
elif gr >= 0.7:
    print("C")
elif gr >= 0.6:
    print("D")
elif gr < 0.6:
    print("F")
