# CTI-110 
# M3LAB - Debugging
# Jermine Mentore
# September 16, 2017
#.

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    # TO DO: define the rest of the scores

    
score = int(input('Enter grade: '))

if score > 90:
    print('Your grade is: A')

score = int(input('Enter grade: '))    

if score > 80:
     print('Your grade is: B')
  
else:
    print('Your grade is: F') # TO DO: finish this







# program start
main()
