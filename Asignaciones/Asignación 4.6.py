hrs = input("Enter hours: ")
rte = input("Enter rate: ")
try:   
    h = float(hrs)
    r = float(rte)
except:
    print("Error, please enter numeric input")
    quit()
def computepay(h, r):
    if h > 40:
        x = h - 40
        y = x * (r*1.5)
        t = h - x
    elif h <= 40:
        y = 0
        t = h
    pay = (t*r)+y
    return pay
print("Pay",computepay(h,r))