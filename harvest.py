############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []

    def __repr__(self):
        return "< name: {}, code: {} >".format(self.name, self.code)


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        return self.pairings

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        return self.code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('Muskmelon', 'musk', 1998, 'green', True, True)
    musk.add_pairing('mint')

    casaba = MelonType('Casaba', 'cas', 2003, 'orange', True, False)
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')

    crenshaw = MelonType("Crenshaw", 'cren', 1996, 'green', True, False)
    crenshaw.add_pairing("proscuitto")

    yellow_watermelon = MelonType("Yellow Watermelon", "yw", 2013, 'yellow',
                                  True, True)
    yellow_watermelon.add_pairing('ice cream')

    all_melon_types.extend([musk, casaba, crenshaw, yellow_watermelon])

    return all_melon_types


def print_melon_pairings(melon_type_list):
    """Given list of MelonType onjects, prints melon pairings."""

    for melon in melon_type_list:
        print "{} pairs with".format(melon.name)
        for pairing in melon.pairings:
            print " - {}".format(pairing)
        print


def make_melon_type_lookup(melon_type_list):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_types = {}

    for melon in melon_type_list:
        melon_types[melon.code] = melon

    return melon_types




############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, mtype, shape_rating, color_rating, field, harvester):
        self.mtype = mtype
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester


    def is_sellable(self):
        """If melon is sellable, return True. Otherwise, return False."""

        return (self.shape_rating > 5 and
                self.color_rating > 5 and
                self.field != 3)

melon1 = Melon("yw", 8, 7, 2, "Sheila")
melon9 = Melon("yw", 7, 10, 3, "Sheila")

def make_melons(melon_types):
    """Returns a list of Melon objects."""




def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""


    # Fill in the rest 



# Create list with make_melon_types(), call make_melon_type_lookup on list
# to return a dictionary of the melon list. The key is equal to the melon code,
# and the value is the instance itself.
melon_dictionary = make_melon_type_lookup(make_melon_types())

melon_1 = Melon(melon_dictionary["yw"], 8, 7, 2, "Sheila")
melon_2 = Melon(melon_dictionary["yw"], 3, 4, 2, "Sheila")
melon_4 = Melon(melon_dictionary["cas"], 10, 6, 35, "Sheila")
melon_5 = Melon