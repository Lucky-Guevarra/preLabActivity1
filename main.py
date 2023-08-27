def expand_text(text):
    return "*" + text + "*"

Prog = "Lucky Angel S. Guevarra"
Prof = "Jasmin Almarines"
due_Date = "09/09/23"
email_Address = "ladew_jasmine@yahoo.com"
letter_J = [
    "            ****",
    "            ****",
    "            ****",
    "     ****   ****",
    "     ****   ****",
    "     **********",
    "     ********",

]

letter_H = [
    "***** *****",
    "***** *****",
    "***********",
    "***********",
    "***** *****",
    " ***** *****",
    "   ***** *****",
]

letter_A = [
    "   ******",
    "  ********",
    "  ***  ***",
    "************",
    "************",
    "****    ****",
    "****    ****",
]
letters = [letter_J, letter_H, letter_A]
asterisk_line = "*" * 58

print(asterisk_line)
print()
print(expand_text("Machine Learning 1".center(56)))
print()
print(expand_text("Fundamentals of Programming".center(56)))
print()
print(expand_text(("Programmer: " + Prog).center(56)))
print()
print(expand_text(("Professor: " + Prof).center(56)))
print()
print(expand_text(("Due Date: " + due_Date).center(56)))
print()
print(expand_text(("Email-address: " + email_Address).center(56)))
print()
print(asterisk_line)
print()
print()
for i in range(len(letters[0])):
    for letter in letters:
        print(letter[i], end="     ")
    print()