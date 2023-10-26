powers = [3, 8, 9, 7, 20, 10]
mini, maxi = 0, 0

for power in powers:
    if mini==0 and maxi==0:
        mini, maxi=powers[0],powers[0]
        print(mini, maxi)
    else:
        mini = min(mini, power)
        maxi = max(maxi, power)
        print(mini, maxi)

#it will print min values on the ;left and max values on teh right
