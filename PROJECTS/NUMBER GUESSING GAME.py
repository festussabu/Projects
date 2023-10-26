import random
import math

lower = int(input("enter lower digit = "))

upper = int(input("enter upper digit = "))

x = random.randint(lower, upper)

print("\n\tyou have ", round(math.log(upper - lower +1, 2)),
      "cahnces\n")

count = 0
while count<math.log(upper - lower +1, 2):
    count+=1
    guess = int(input("enter an integer: "))
    if x == guess:
        print("correct guess; ", "you took", count, "guess only")
        count = 0
        break

    elif x > guess:
        print("too small")
    elif x < guess:
        print("too big")

if count >= math.log(upper - lower +1, 2):
    print("\nsry you failed")
    print("number is %d" % x)
    print("\nBETTER LUCK NEXT TIME!")
