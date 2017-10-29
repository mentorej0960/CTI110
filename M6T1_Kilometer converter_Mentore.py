# CTI-110 
# M6T1 - Kilometer Converter
# Jermine Mentore
# October 29, 2017
#.

conversion_factor = 0.621371

def main():
    
    kilometers = float( input( "Please enter the number of kilometers: "))

    show_miles(kilometers)

def show_miles(km):

    miles = km * conversion_factor

    print(km, "kilometers equals", miles, "miles.")
           



main()







