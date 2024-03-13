#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number - (number // 10)
if last_digit > 5:
    post_remark = "and is greater than 5"
else:
    if last_digit == 0:
        post_remark = "and is 0"
    else:
        post_remark = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {post_remark}")
