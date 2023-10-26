import random
import string

passwd = str("344")

ch = list(string.digits)
# ch = list(string.printable)
# print(ch)


while True:
    var = random.choices(ch, k = len(passwd))
    print(">>>>>>>>>>", var, "<<<<<<<<<<")
    join = "". join(var)
    if join == passwd:
        print('Your pass is: ', join)
        break

