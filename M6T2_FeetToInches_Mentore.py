#Converting feet to inches
#October 29, 2017   
#CTI-110 M6T2_FeetToInches
#Jermine Mentore
#

INCHES_PER_FOOT = 12

def main():
    
    feet = int( input( "Please enter the number of feet: "))

    print(feet, "equals", feet_to_inches(feet), "inches.")

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

    
           

main()







  
    

