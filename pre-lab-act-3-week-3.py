#A supermarket clerk has run out of changes except for 25 centavo coins. Create a program that asks for the amount of purchase and the amount given. The program should calculate the number of quarters given as change and the amount of change still due. Set your surname as the name of the supermarket (title). Use scripting mode. attach a screenshot of the code and output.
def texto(text):
    return "*" + text + "*"
try:
    a = [int(input("how much is the item you are buying (pesos): ")), int(input("how much is the item you are buying (per 25 centavos): "))]
    b = int(input("indicate the amount you wish to buy: "))
    c = [int(input("state the amount you are giving (pesos): ")), int(input("state the amount you are giving (25 centavos): "))]
except ValueError:
    print("Must be a number")
    exit()
full = a[0] * 4 + a[1]
fullg = c[0] * 4 + c[1]
d = full * b
e = d - fullg
f = fullg - d
g = [e / 4, f / 4]
asterisk = "*" * 80
sm = "Supermarket"
owner = "Guevarra"
thingy = owner + sm 
if d > fullg:
    print(asterisk)
    print()
    print(texto(thingy.center(78)))
    print(texto(("insufficient amount to purchase, you need: " + str(e) +" in 25₵ more"+" or ₱"+ str(g[0]) +" more").center(78)))
    print()
    print(asterisk)
elif d == 0:
    print(asterisk)
    print()
    print(texto(thingy.center(78)))
    print(texto("you're holding the line, you're not going to buy anything anyway".center(78)))
    print()
    print(asterisk)
elif d == fullg:
    print(asterisk)
    print()
    print(texto(thingy.center(78)))
    print(texto("Thank you for your purchase!".center(78)))
    print()
    print(asterisk)
else:
    print(asterisk)
    print()
    print(texto(thingy.center(78)))
    print(texto(("your change is: " + str(f) +" in 25₵"+" or ₱"+ str(g[1])+" .Thank you for your purchase!").center(78)))
    print()
    print(asterisk)
