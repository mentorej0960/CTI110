# CTI-110 
# M3HW1 - Software Sales
# Jermine Mentore
# September 23, 2017


def main():

   numberofPackages = float( input("Please enter number of packages purchased:"))

   priceofPackage = 99

   if numberofPackages < 10:
        discount = 0

   elif numberofPackages < 20:
       discount = 0.10

   elif numberofPackages < 50:
       discount = 0.20

   elif numberofPackages < 100:
       discount = 0.30

   else:
      discount = 0.40
   
   subTotal = numberofPackages * priceofPackage
   print("Cost before discount:", subTotal)

   discountAmount = discount * subTotal
   print("Cost of discount:", discountAmount)

   total = subTotal - discountAmount
   print("Cost after dicount:", total)

               


    
    
main()    


   
