############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.name = name
        self.color = color
        self.is_bestseller = is_bestseller
        self.is_seedless = is_seedless
        self.first_harvest = first_harvest

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    muskmelon = MelonType("musk", 1998, "Green", True, True, "Muskmelon")
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType("cas", 2003, "Orange", True, False, "Casaba")
    #should look at later for more efficient method
    casaba.add_pairing("strawberry")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", 1996, "Green", True, False, "Crenshaw")
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw", 2013, "Yellow", True, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

melons = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with:")
        for pairing in melon.pairings:
            print(f"-{pairing}")

# print_pairing_info(melons)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melons_by_id = {}
    for melon in melon_types:
        if melon.code not in melons_by_id:
            melons_by_id[melon.code] = melon

    return melons_by_id

# melons_by_id = make_melon_type_lookup(melons)


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__ (
            self, melon_type, shape_rating, color_rating, field_number, harvester
    ):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_number = field_number
        self.harvester = harvester

        def is_sellable(self):
            if self.shape_rating > 5 and self.color_rating > 5 and self.field_number != 3:
                return True
            else:
                return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons_by_id = make_melon_type_lookup(melon_types)
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    harvested_melons = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]
    return harvested_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    for melon in melons:
        if melon.is_sellable() == True:
            print(f"Harvested by {melon.harvester} from field {melon.field_number} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon.harvester} from field {melon.field_number} (CANNOT BE SOLD)")

get_sellability_report(make_melons(melons))