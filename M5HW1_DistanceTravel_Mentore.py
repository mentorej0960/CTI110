# CTI-110 
# M5HW1 - Distance Travel
# Jermine Mentore
# September 16, 2017

def main():

    vehicleSpeed = float(input("What is the speed of the vehicle in MPH?: " ))
    timeTraveled = int(input("How many hours has it traveled?: "))

    print("Hour","\Distance Traveled: ")
    for currentHour in range(1, timeTraveled + 1):
        distanceTraveled = vehicleSpeed * currentHour
        print(currentHour,"\t",distanceTraveled)
        

main()
