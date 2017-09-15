# CTI-110 
# M2HW2 - Tax Tips and Total 
# Jermine Mentore
# September 15, 2017
#.
foodCharge = float( input( "please enter the charge of the food: " ))
tip = 0.18 * foodCharge
salesTax = 0.07 * foodCharge
total = foodCharge + tip + salesTax
print( "Food Charge: $", format(foodCharge, ",.2f"))
print("tip: $", format(tip, ",.2f"))
print("sale tax: $",format(salesTax,",.2f"))
print("total: $", format(total, ",.2f"))

