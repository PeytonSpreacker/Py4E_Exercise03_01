hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float (rate)
#print(h, r)
if h > 40:
    #print("Overtime")
    reg = h * r
    otp = (h-40.0) * (r * 0.5)
    #print(reg, otp)
else :
    print("Regular")
    reg = h * r
    otp = 0
pay = reg + otp
print(pay)