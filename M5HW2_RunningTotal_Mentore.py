#CTI-110
#M5HW2: Running Total
#Jermine Mentore
#October 20, 2017


def main():
    total = 0
    number = 0

    number = int(input("Please enter whole number. Negative number to exit: "))

    while number >= 0:
        total = number + total

        number = int(input("Please enter whole number.Negative number to exit: "))

    print("The total is: ", total)


main()
        
