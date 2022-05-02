# first get the customer details -- save them in a list

# then get the number of pizzas that the customer wants to order

# loop the number of pizza's through with each order 

# in loop function input size, toppings, delivery return as list 

# in loop function work out the cost of the pizza, return as float

# add the pizza cost to total

# out of loop : is discount?

# if delivery, add 2.5

""" 
output:
customer details
cost of the pizzas
discount given
delivery cost
total cost
"""
def pizza_input():
    """This will be the function that records the input for the pizzas that the
        customer would like to order"""
    
    size = ""
    valid_sizes = ["s", "small", "m", "medium", "l", "large"]
    while not size in valid_sizes :
        size = input("What size pizza would the customer like to purchase: small(s), medium(m), or large(l)?")
    
    toppings = input("What toppings would the customer like to purchase? (Please enter with a space between each topping)")
    toppings = toppings.split(" ")
    
    return [size, toppings]

def pizza_cost(list):
    """This will be a function that calculates the cost of the pizza from the variables provided."""
    if list[0].lower() == "s" or list[0].lower() == "small":
        cost = 3.25
    elif list[0].lower() == "m" or list[0].lower() == "medium":
        cost = 5.5
    elif list[0].lower() == "l" or list[0].lower() == "large":
        cost = 7.15
    
    no_toppings = len(list[1])
    
    if no_toppings == 1:
        cost += 0.75
    elif no_toppings == 2:
        cost += 1.35
    elif no_toppings == 3:
        cost += 2
    elif no_toppings >= 4:
        cost += 2.5
    
    return cost




total_cost = 0
pizza_total = 0
delivery_charge = 0
discount = 0
order = []

customer_name = input("Please enter the name of the customer: ")
customer_address = input("Please enter the address of the customer: ")
customer_phone_number = input("Please enter the phone number of the customer: ")

number_of_pizzas = int(input(f"Please enter the number of pizzas that {customer_name} would like to purchase"))

for pizza in range(number_of_pizzas):
    pizza_x = pizza_input()
    cost = pizza_cost(pizza_x)
    total_cost += cost
    pizza_total += cost

if total_cost > 20:
    discount = total_cost * 0.1
    total_cost -= discount
    

delivery = input("Does the customer want a delivery?")

if delivery.lower() == "y" or delivery.lower() == "yes":
    delivery_charge = 2.5
    total_cost += delivery_charge

print(f"Order for: {customer_name}")
print(f"Customer address: {customer_address}")
print(f"Customer Phone Number: {customer_phone_number}")

print(f"The total cost of the pizza's was: £{pizza_total}")
print(f"The total discount applied was: £{discount}")
print(f"The total delivery charge was: £{delivery_charge}")
print(f"The total cost of the order is: £{total_cost}")


# tomorrow I will set out to learn to code a way to make a user interface so that I can use buttons rather than using the command line