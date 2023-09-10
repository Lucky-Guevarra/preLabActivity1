#If you run a 10-kilometer race in 43 minutes and 30 seconds,
#what is your average time per mile?
#What is your average speed in miles per hour?
#(Hint: there are 1.61 kilometers in a mile).
def textto (text):
    return "*" + text + "*"
asterisk = "*" * 58

km_to_m = 10 / 1.61

a = round(43.5/km_to_m, 2)
b = round(km_to_m/(43.5/60),2)

print(asterisk)
print()
print(textto(("Average time per mile: "+str(a)+" min/mile").center(56)))
print()
print(textto(("Average Speed in miles per hour: "+str(b)+" m/h").center(56)))
print()
print(asterisk)
