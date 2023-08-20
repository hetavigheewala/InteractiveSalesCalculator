
# Brief explanation of the program:
# This program interacts with the user to display your name,
# check if their last name is "Python", determine if a number
# is between 0 and 10, and calculate the cost of items sold with discounts.

# Displays my full name
print("My Name: Hetavi Gheewala")

# Asks the user to enter their last name and display it
last_name = input("Enter your last name: ")
print("Your name is:", last_name)

# Checks if the last name is "Python" and displays the appropriate message
if last_name == "Python":
    print("You share a name with a programming language")
else:
    print("Not a language!")

# Asks the user to input a number and displays a message based on its range
number = int(input("Enter a number: "))
if 0 <= number <= 10:
    print("HELLO")
else:
    print("Greetings")

# Asks the user for the quantity of items sold
quantity = int(input("Enter the number of items sold: "))

# Checks if the quantity is valid and perform calculations
if quantity <= 0:
    print("Invalid number of items - Use a quantity of 1 or more")
else:
    unit_cost = float(input("Enter the unit cost of the product: $"))

    # Determine the discount percentage based on the quantity
    if 1 <= quantity <= 19:
        discount_percentage = 20
    elif 20 <= quantity <= 49:
        discount_percentage = 30
    elif 50 <= quantity <= 99:
        discount_percentage = 40
    else:
        discount_percentage = 50

    # Calculates the cost before discount
    cost_before_discount = quantity * unit_cost

    # Calculates the amount of discount
    amount_of_discount = cost_before_discount * (discount_percentage / 100)

    # Calculates the final cost after discount
    final_cost = cost_before_discount - amount_of_discount

    # Displays the results
    print("Quantity of items sold:", quantity)
    print("Unit cost: $", "{:.2f}".format(unit_cost))
    print("Cost before discount: $", "{:.2f}".format(cost_before_discount))
    print("Discount percentage:", discount_percentage, "%")
    print("Amount of discount: $", "{:.2f}".format(amount_of_discount))
    print("Final cost after discount: $", "{:.2f}".format(final_cost))
