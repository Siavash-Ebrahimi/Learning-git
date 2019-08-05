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
'''
Greeting = ["Hi", "Holla", "Hello", "Welcome", "Salam",
            "Marhaba", "Saboolik", "سلام"]
H = input("What is your name: ")
#------------------------------------------------------
x=0;
while x != 5:
    print(random.choice(Greeting), H)
    x += 1

'''
