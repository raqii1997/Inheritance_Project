# The office_furniture class holds general information
# about office furniture items for sale
# it will be the parent class for desks, chairs, filling cabinets, etc.


class Office_furniture(object):
    """

    Attributes: category, Material, Length, Width, Height, quantity, Price, Cute

    """

    # in my __init__() function I am using "Hidden" attribute names
    def __init__(self, category, material, length, width, height, quantity, price, quality):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__quantity = quantity
        self.__price = price
        self.__quality = quality

        # setters and getters
        # Set methods set a value for a hidden attribute
        # get methods return the value of a hidden value

    def set_category(self, category):
        self.__category = category

    def get_category(self):
        return self.__category

    def set_material(self, material):
        self.__material = material      # don't forget to make it hidden!

    def get_material(self):
        return self.__material

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_total_price(self, total_price):
        self.__total_price = total_price

    def get_total_price(self):
        return self.__price * self.__quantity

    def set_quality(self, quality):
        self.__quality = quality

    def get_quality(self):
        return self.__quality



    def __str__(self):
        line_item = "Product: " + self.__category + "   Material: " + self.__material + "   Length: " + str(
            self.__length) + "   Width: " + str(self.__width) + "   Height: " + str(self.__height) + "   Quantity: " + str(
            self.__quantity) + "   Each: ${:0,.2f}".format(self.__price) + "   Total= ${:0,.2f}".format(
            self.get_total_price())
        return line_item


class Desk(Office_furniture):
    """
    attributes: drawer_location, number_drawers
    inherited attribute: category, material, cute
    """

    # When I initialize my object I need to make sure both parent and child attributes are set
    def __init__(self, category, material, length, width, height, number_drawers, drawer_location, quantities, price, cute):
        Office_furniture.__init__(self, category, material, length, width, height, quantities, price, cute)      # this statement __init__ parent attribute
        self.__drawer_location = drawer_location
        self.__number_drawers = number_drawers
        self.__quantities = quantities
    # this method overrides the parent class method

    def set_drawer_location(self, drawer_location):
        self.__drawer_location = drawer_location

    def get_drawer_location(self):
        return self.__drawer_location

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def get_number_drawers(self):
        return self.__number_drawers

    #def set_quantities(self, quantities):
        #self.__quantities = quantities

    #def get_quantities(self):
        #return self.__quantities

    # this method overrides the parent class method
    def __str__(self):
        line_item = "Product: " + self.get_category() + "   Material: " + self.get_material() + "   Length: " + str(
            self.get_length()) + "   Width: " + str(self.get_width()) + "   Height: " + str(
            self.get_height()) + "   Number of Drawers: " + str(
            self.get_drawer_location()) + "   Drawer Location: " + self.get_drawer_location() + "   Quantity: " + str(
            self.get_quantity()) + "   Each: ${:0,.2f}".format(self.get_price()) + "   Total= ${:0,.2f}".format(
            self.get_total_price())
        return line_item
