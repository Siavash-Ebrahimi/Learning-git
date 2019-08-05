import os
import sys
import random

Greeting = ["Hi", "Holla", "Hello", "Welcome", "Salam",
            "Marhaba", "Saboolik", "سلام"]
H = input("What is your name: ")
x=0;
while x != 5:
    print(random.choice(Greeting), H)
    x += 1

