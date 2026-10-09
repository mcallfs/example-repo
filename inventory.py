
# We create a Shoe class which will be used as a template
# for every shoe object we create in the program
class Shoe:

    # The __init__ method sets up the information that every shoe will contain
    # self allows each shoe object to store its own values
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

        # We remove pass because we are now giving the method something to do
        # pass is only a placeholder and tells Python to do nothing at that point
        # pass - we remove this


    # This method allows us to return the object stored against a shoe cost
    def get_cost(self):
        return self.cost

        # pass - we remove this


    # This method allows us to return the quantity stored against a shoe object
    def get_quantity(self):
        return self.quantity
    
        # pass - we remove


    # __str__ controls how the shoe information will look when we print the object
    # We use an f-string to combine all of the shoe attributes into one readable line
    def __str__(self):
        return f"({self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity})"
        
        # pass - We remove


# We create an empty list which will be used to store all of our Shoe objects
shoe_list = []

# This function reads the existing shoe information from inventory.txt
def read_shoes_data():

    # We use try/except so the program can handle the text file not being found
    # instead of the whole program crashing
    try:

        # Open inventory.txt in read mode using the with open function
        # This automatically closes the file once we have completed the task
        with open("inventory.txt", "r") as file:

            # readlines() reads all the lines from the file
            # and stores them so we can work through the
            lines = file.readlines()

            # We loop through each line
            # [1:] skips the first line because this contains the column headings
            for line in lines[1:]:
                data = line.strip().split(",")

                # We use the index positions to get each piece of shoe information
                country = data[0]
                code = data[1]
                product = data[2]
                cost = float(data[3])
                quantity = int(data[4])

                # Create a new shoe object using the info read from the file
                shoe = Shoe(country, code, product, cost, quantity)

                # update the shoe list with newly created object
                shoe_list.append(shoe)

    # If inventory.txt cannot be found we display a useful message
    # rather than allowing the program to crash
    except FileNotFoundError:
        print("The inventory.txt file could not be found.")

    # we remove pass
    

# This function allows the user to manually add a new shoe
def capture_shoes():

    # We use try/except because cost and quantity need to be valid numbers
    try:

        # Ask the user to enter each piece of information for the new shoe
        country = input("Please enter the country: ")
        code = input("Please enter product code: ")
        product = input("Please enter product name: ")
        cost = float(input("Please enter cost: "))
        quantity = int(input("Please enter quantity in stock: "))

        # We use the information entered by the user to create a new Shoe object
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

        # we open the inventory text file with the function of appending
        with open("inventory.txt", "a") as file:

            # we use the get fucntion for cost and quantity
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.get_cost()},{shoe.get_quantity()}\n")

    # If the user enters an invalid number for cost or quantity
    # we catch the ValueError and display a message
    except ValueError:
        print("Please enter a valid number for cost and quantity")

    # We remove pass


# This function displays all of the shoes currently stored in shoe_list
def view_all():
    # We use a for loop to work through every Shoe object in the list
    for shoe in shoe_list:
        print(shoe)

    # we remove pass


# This function finds the shoe with the lowest stock quantity
# and gives the user the option to restock it
def re_stock():

    # min() finds the lowest value
    # The lambda tells Python that we specifically want to compare shoe.quantity
    lowest_stock = min(shoe_list, key=lambda shoe: shoe.get_quantity())

    # Display the product and its current quantity
    print(lowest_stock.product)
    print(lowest_stock.get_quantity())

    # Ask the user whether they want to restock this shoe
    restock_choice = input("Would you like to restock this item? (yes/no):")
    if restock_choice.lower() == "yes":
        restock_amount = int(input("Please enter the amount: "))
        updated_stock = restock_amount + lowest_stock.get_quantity()
        lowest_stock.quantity = updated_stock

        # Open inventory.txt in write mode using the with open function
        # "w" means we are rewriting the file with the updated information
        # This automatically closes the file once we have completed the task
        with open("inventory.txt", "w") as file:

            # Write the column headings back into inventory.txt
            file.write("Country, Code, Product, Cost, Quantity\n")

            # Loop through every shoe stored in shoe_list
            for shoe in shoe_list:

                # Write each shoe's information back into the file
                # Use the get methods to retrieve the cost and quantity
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.get_cost()},{shoe.get_quantity()}\n")

    # We remove pass


def search_shoe():
    search_code = input("Please enter the shoe code: ")

    # Loop through all of the Shoe objects in shoe_list
    for shoe in shoe_list:
        if shoe.code == search_code:
            return shoe

    # We remove pass


def value_per_item():

    # Loop through every shoe in shoe_list
    for shoe in shoe_list:

        # Calculate the value by multiplying the cost by the quantity in stock
        value = shoe.get_cost() * shoe.get_quantity()
        print(shoe.product)
        print(value)

    # we remove pass


def highest_qty():

    # max() finds the highest value
    # The lambda tells Python to compare the quantity attribute of each shoe
    highest_stock = max(shoe_list, key=lambda shoe: shoe.get_quantity())
    print(highest_stock.product, "is for sale")
    print("Quantity", highest_stock.get_quantity())

    # we remove pass


# Before displaying the menu we call read_shoes_data()
# This loads all the existing shoes from inventory.txt into shoe_list
read_shoes_data()

# We use while True because we want the menu to continue running
# until the user chooses option 7 to exit
# Display all of the available options to the user
while True:
    print("Inventory Menu")
    print("1 - Capture a new shoe")
    print("2 - View all shoes")
    print("3 - Restock shoes")
    print("4 - Search for a shoe")
    print("5 - View value of item")
    print("6 - View highest quantity")
    print("7 - Exit")

    # Ask the user to select an option
    # input returns a string so we compare the choice with "1", "2" etc.
    menu_choice = input("Please choose an option from the inventory menu: ")
    if menu_choice == "1":
        capture_shoes()

    # We use multiple elif statements so the algorithm is able to checking the below
    # functions more efficiently and stops when it has found the correct condition
    elif menu_choice == "2":
        view_all()
    elif menu_choice == "3":
        re_stock()
    elif menu_choice == "4":
        print(search_shoe())
    elif menu_choice == "5":
        value_per_item()
    elif menu_choice == "6":
        highest_qty()
    elif menu_choice == "7":
        exit()
