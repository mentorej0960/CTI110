# CTI-110 
# M3HW1 - Age Classifier 
# Jermine Mentore 
# September 16, 2017
#
def main():

    AgeOfUser = int(input("please enter person's age:"))

    if AgeOfUser <=1:
        print("This is an infant access denied parents permission needed.")

    elif AgeOfUser <= 13:
        print("This is an child access denied parents permission needed.")

    elif AgeOfUser <= 20:
        print("This is a teenager access denied parents permission needed.")

    else:
        print("This is an adult access granted") 










main()


 


