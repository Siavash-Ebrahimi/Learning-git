import os
import sys
import random

#-- Adding Dictionary --------------------
H = input("What is your name: ")
c = input('Where are you from? ')
Greeting = {"Iran":"سلام", "Spain":"Holla", "England":"Hi"}
Country = ['Iran', 'Spain', 'England']
##print(Ra_Country)
x = 0;
for i in Country:
    if i == c:
        print(Greeting[Country[x]], H, 'From', c)
    x += 1
#------------------------------------------------------
print("========================================")
print("---------Random|Greeting----------------", '\n')

Greeting = ["Hi", "Holla", "Hello", "Welcome", "Salam",
            "Marhaba", "Saboolik", "سلام"]
x1=0;
while x1 != 5:
    print(random.choice(Greeting), H)
    x1 += 1


