#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    str = "is positive"
elif number < 0:
    str = "is negative"
else:
    str = "is zero"
print(f"{number} {str}")
