# CTI-110 
# M5T2 - Bug Collection
# Jermine Mentore
# October 14, 2017



def main():

    total = 0

    for day in range(1, 8):
        print("Enter the bugs collected on day", day)


        bugsCollected = int( input("Please enter number of bugs collected: "))


        total += bugsCollected

         
    print("The total number of bugs collected equals to", total, "bugs.")



main()
