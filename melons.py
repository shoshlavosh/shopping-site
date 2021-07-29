"""Ubermelon melon types.

This provides a Melon class, helper methods to get all melons, find a
melon by id.

It reads melon data in from a text file.
"""

# Defines a Melon class with all the attributes
class Melon(object):
    """An Ubermelon Melon type."""

    def __init__(self,
                 melon_id,
                 melon_type,
                 common_name,
                 price,
                 image_url,
                 color,
                 seedless,
                 ):
        self.melon_id = melon_id
        self.melon_type = melon_type
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless

    # Melon class method that returns a price string formatted with decimals - $2.00
    def price_str(self):
        """Return price formatted as string $x.xx"""

        return "${:.2f}".format(self.price)

    # ID information about a melon object (we haven't learned this yet)
    def __repr__(self):
        """Convenience method to show information about melon in console."""

        return "<Melon: {}, {}, {}>".format(self.melon_id, self.common_name, self.price_str())

# Function that reads melon information from melons.txt
def read_melon_types_from_file(filepath):
    """Read melon type data and populate dictionary of melon types.

    Dictionary will be {id: Melon object}
    """
    # Creates a melon_types dictionary
    melon_types = {}

    # Opens file, loops through each line, splits up info and assigns variables to each chunk of info (its a list)
    with open(filepath) as file:
        for line in file:
            (melon_id,
             melon_type,
             common_name,
             price,
             img_url,
             color,
             seedless) = line.strip().split("|")

            # converts price into a float type
            price = float(price)
    
            # For seedless, we want to turn "1" => True, otherwise False
            seedless = (seedless == "1")
    
            # Adds Melon object to melon_types dictionary key = [melon_id], value = Melon object
            melon_types[melon_id] = Melon(melon_id,
                                          melon_type,
                                          common_name,
                                          price,
                                          img_url,
                                          color,
                                          seedless)

    return melon_types

# Function that gets a list of Melon objects from the melon_types dictionary above 
def get_all():
    """Return list of melons.

        If you call this function, you should get back a list like the one below.
        NOTE: This is an example of a doctest.

        >>> get_all()
        [<Melon: 2, Crenshaw, $2.00>, <Melon: 14, Ali Baba Watermelon, $2.50>, <Melon: 15, Ancient Watermelon, $3.00>, <Melon: 16, Arkansas Black Watermelon, $4.00>, <Melon: 21, Chris Cross Watermelon, $2.50>, <Melon: 23, Congo Watermelon, $2.00>, <Melon: 25, Crimson Sweet Watermelon, $1.75>, <Melon: 27, Desert King Watermelon, $2.00>, <Melon: 28, Dixie Queen Watermelon, $2.00>, <Melon: 29, Moonbeam Watermon, $2.25>, <Melon: 30, Fairfax Watermelon, $2.00>, <Melon: 32, Golden Honey Watermelon, $2.50>, <Melon: 33, Golden Midget Watermelon, $2.50>, <Melon: 34, Hopi Yellow Watermelon, $2.50>, <Melon: 35, Irish Grey Watermelon, $2.50>, <Melon: 37, Jubilee Bush Watermelon, $2.50>, <Melon: 38, Jubilee Watermelon, $2.50>, <Melon: 42, Ledmon Watermelon, $3.00>, <Melon: 44, Malali Watermelon, $2.00>, <Melon: 45, Melitopolski Watermelon, $3.00>, <Melon: 48, Montenegro Man Melon, $2.50>, <Melon: 49, Moon and Stars Watermelon, $2.50>, <Melon: 52, Navajo Winter Watermelon, $3.00>, <Melon: 54, Orangeglo Watermelon, $2.75>, <Melon: 56, Royal Golden Watermelon, $2.25>, <Melon: 57, Scaly Bark Watermelon, $4.00>, <Melon: 58, Stone Mountain Watermelon, $3.00>, <Melon: 59, Sugar Baby Watermelon, $2.50>, <Melon: 60, Takii Gem Watermelon, $2.75>, <Melon: 61, Tendergold Watermelon, $2.50>, <Melon: 62, Texas Golden Watermelon, $2.75>, <Melon: 63, Thai Rom Dao Watermelon, $2.50>, <Melon: 64, Tom Watson Watermelon, $2.25>, <Melon: 66, White Wonder Watermelon, $2.50>, <Melon: 67, Wilson's Sweet Watermelon, $2.50>]
    """

    # This relies on access to the global dictionary `melon_types`

    return list(melon_types.values())

# Function that takes in a melon_id and returns melon object information
def get_by_id(melon_id):
    """Return a melon, given its ID."""

    # This relies on access to the global dictionary `melon_types`

    return melon_types[melon_id]


# Dictionary to hold types of melons.
#
# Format is {id: Melon object, ... }

# Calls read_melon_types_from_file function and adds melons.txt as arguement passed in
melon_types = read_melon_types_from_file("melons.txt")
