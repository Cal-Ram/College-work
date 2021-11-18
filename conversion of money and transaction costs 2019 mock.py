# money wanted to convert - done
# currency requested - done
# convert currency - done
# transaction fee - done 
# total cost to convert - done
# apply a 5% discount if staff - done

money_to_convert = int(input("How much money does the customer wish to convert?"))
convert_to = input("Which currency does the customer wish to buy?")
is_staff = input("Is the customer a member of staff?")

if convert_to == "USD":
    new_money = money_to_convert * 1.4
elif convert_to == "EUR":
    new_money = money_to_convert * 1.14
elif convert_to == "BRL":
    new_money = money_to_convert * 4.77
elif convert_to == "JPY":
    new_money = money_to_convert * 151.05
elif convert_to == "TRY":
    new_money = money_to_convert * 5.68
else:
    print("Invalid currency")
print("The total money in the new currency is: ", new_money)

if money_to_convert < 300:
    total_cost = money_to_convert * 1.035
elif money_to_convert < 750:
    total_cost = money_to_convert * 1.03
elif money_to_convert < 1000:
    total_cost = money_to_convert * 1.025
elif money_to_convert < 2000:
    total_cost = money_to_convert * 1.02
elif money_to_convert >= 2000 and money_to_convert <= 2500:
    total_cost = money_to_convert * 1.015
else:
    print("Invalid amount of money")
if is_staff == "yes":
    total_cost = total_cost * 0.95
print("The total cost of this transaction is: £", total_cost)