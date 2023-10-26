

CURRENT_BALANCE = 1000



def chek_pin(num):
    PIN = 1111
    if num == PIN:
        return True
    else:
        return False



def main():
    print("WELCOME TO   A T M")
    "\t"
    z = 1
    while z==1:
     a = int(input("ENTER PIN: "))
     if chek_pin(a)==True:
        print("CORRECT PIN")

        WITHDRAW = input("DO YOU WANT TO WITHDRAW? ")
        if WITHDRAW=="yes" or WITHDRAW == "YES":
            WITHDRAW_AMOUNT = int(input("ENTER AMOUNT: "))
            if WITHDRAW_AMOUNT<0:
                print("ENTER POSITIVE NUMBER! ")
                continue

            elif WITHDRAW_AMOUNT<=CURRENT_BALANCE:
             AMOUNT_LEFT = CURRENT_BALANCE - WITHDRAW_AMOUNT
             print("YOU SUCCESSFULLY WITHDRAWN ", WITHDRAW_AMOUNT, "RUPEES")
             print("YOUR CURRENT BALANCE =",AMOUNT_LEFT)
            elif WITHDRAW_AMOUNT > CURRENT_BALANCE:
                print("YOU DON'T HAVE ENOUGH BALANCE")
                TRY1 = input("DO YOU WANT TO TRY AGAIN? ")
                if TRY1=="YES" or TRY1=="yes":
                   continue
                else:
                    break



            break

        else:
            print("thankyou")
            print("come back later")
            break

     else:
             print("WRONG PIN")
             TRY = input("DO YOU WANT TO TRY AGAIN? ")
             if TRY == "YES" or TRY == "yes":
                 z = 1
             else:
                print("THANKYOU")
                z = 0

main()








































