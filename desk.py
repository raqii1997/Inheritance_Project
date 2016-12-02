# import Inheritance.py
import Inheritance

# function for implementing object from Inheritance


def main():
    # creating an object of the Furniture sub class for Desk
    desk = Inheritance.Desk("Desk", "Wood", 50, 25, 30, 4, "Left", 2, 150.00, "Good")

    # printing the information
    print"\n\n=======================================================>"
    print("Product: " + desk.get_category())
    print("Material: " + desk.get_material())
    print("Length: " + str(desk.get_length()))
    print("Width: " + str(desk.get_width()))
    print("Height: " + str(desk.get_height()))
    print("Number of Drawers: " + str(desk.get_number_drawers()))
    print("Location of Drawers: " + desk.get_drawer_location())
    print("Quantity: " + str(desk.get_quantity()))
    print("Price per Quantity: " + str(desk.get_price()))
    print("Price: ${:0,.2f}".format(desk.get_total_price()))
    print("quality :" + str(desk.get_quality()))
    print"=======================================================>\n"
    print desk

# call the function
main()
