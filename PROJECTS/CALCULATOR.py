
def sum(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b



def main():
    a = int(input("enetr a number: "))
    b = int(input("enetr 2nd number: "))
    op = int(input("enetr a didgit: "))
    if op == 1:
        print(sum(a, b))
    elif op == 2:
        print(sub(a, b))
    elif op == 3:
        print(mul(a, b))
    elif op == 4:
        print(div(a, b))
    else:
        print("invalid number")
main()



















