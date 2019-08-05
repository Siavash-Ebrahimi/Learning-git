import os
import sys
import random

#-- Adding Dictionary --------------------
Ra_Country = {"Iran":"سلام", "Spain":"Holla", "England":"Hi"}
#------------------------------------------------------

Greeting = ["Hi", "Holla", "Hello", "Welcome", "Salam",
            "Marhaba", "Saboolik", "سلام"]
H = input("What is your name: ")
#---Branch Code--------------------
print(Ra_Country["Iran"], H)
#------------------------------------------------------
x=0;
while x != 5:
    print(random.choice(Greeting), H)
    x += 1

