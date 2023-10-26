import time
import random

OPERATORS = ["+", "-", "*"]
MIN_VALUE = 2
MAX_VALUE = 12
END = 10
def Working():
    left = random.randint(MIN_VALUE, MAX_VALUE)
    right = random.randint(MIN_VALUE, MAX_VALUE)
    operation = random.choice(OPERATORS)

    result = str(left) + " " + operation + " " + str(right)
    ans = eval(result)
    return result, ans

press = input("press enter to start!")
print("------------------------------")
start_time = time.time()

for i in range(END):
    result, ans = Working()
    while True:
        guess = input("Number #" + str(i+1) + ": " + result + " = " )
        if guess == str(ans):
            break
end_time = time.time()
total_time = round(end_time - start_time, 2)

print("------------------------------")
print("nice work", "you took", total_time, "seconds")


