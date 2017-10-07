FoodCharge = float( input( "please enter the charge of the food: " ))
tip = 0.18 * foodCharge
salesTax = 0.07 * foodCharge
total = foodCharge + tip + salesTax
print( "Food Charge: $" + format(foodCharge, ",.2f"), "tip: $" + \ format(tip, ",.2f"), "Sales Tax: $" + Format(salesTax, ",.2f"), \ "total: $" + format(total, ",.2f"), sep = "\n" )
