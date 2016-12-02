import Inheritance


def main():
    # creating an object of the Furniture
    chairs = Inheritance.Office_furniture("Chairs", "Wood", 15, 16, 24, 3, 75.50, "Excellent")

    # printing the information
    print"\n\n=======================================================>"
    print("Product: " + chairs.get_category())
    print("Material: " + chairs.get_material())
    print("Length: " + str(chairs.get_length()))
    print("Width: " + str(chairs.get_width()))
    print("Height: " + str(chairs.get_height()))
    print("Quantity: " + str(chairs.get_quantity()))
    print("Price: ${:0,.2f}".format(chairs.get_price()))
    print("quality :" + str(chairs.get_quality()))
    print"=======================================================>\n"

    print chairs

# call the function

main()
