from abc import ABC, abstractmethod


class House(ABC):
    """
    This class have the abstract methods to know what materials are
    used to build a house of different types.
    """
    @abstractmethod
    def wood(self):
        """
        An empty abstract method to display what wood types are used
        for building a house.
        """
        ...

    @abstractmethod
    def brick(self):
        """
        An empty abstract method to display what brick types are used
        for building a house.
        """
        ...

    @abstractmethod
    def bars(self):
        """
        An empty abstract method to display what iron bars types are used
        for building a house.
        """
        ...

    @staticmethod
    def base():
        """
        A static method to display that every house will have the same
        base irrespective of their materials.
        """
        return f"Base is same for every house types."


class Modular(House):
    """
    This class represents how modular houses are built using
    different types of required materials and other additional
    materials.
    """
    def __init__(self, wood_name, wood_type, brick_type, bars_name, bars_quality,
                 paint_color, paint_primer):
        self.wood_name = wood_name
        self.wood_type = wood_type
        self.brick_type = brick_type
        self.bars_name = bars_name
        self.bars_quality = bars_quality
        self.paint_color = paint_color
        self.paint_primer = paint_primer

    def wood(self):
        return f"Required Wood - For Modular House\n" \
               f"Wood Name: {self.wood_name}\n" \
               f"Wood Type: {self.wood_type}"

    def brick(self):
        return f"Required Brick - For Modular House\n" \
               f"Brick Type: {self.brick_type}"

    def bars(self):
        return f"Required Bars - For Modular House\n" \
               f"Bars Name: {self.bars_name}\n" \
               f"Bars Type: {self.bars_quality}"

    def paint(self):
        return f"Required Paint - For Modular House\n" \
               f"Paint Color: {self.paint_color}\n" \
               f"Paint Primer: {self.paint_primer}"


class Townhouse(House):
    """
    This class represents how townhouses are built using
    different types of required materials and other additional
    materials.
    """
    def __init__(self, wood_name, wood_type, brick_type, bars_name, bars_quality):
        self.wood_name = wood_name
        self.wood_type = wood_type
        self.brick_type = brick_type
        self.bars_name = bars_name
        self.bars_quality = bars_quality

    def wood(self):
        return f"Required Wood - For Townhouse\n" \
               f"Wood Name: {self.wood_name}\n" \
               f"Wood Type: {self.wood_type}"

    def brick(self):
        return f"Required Brick - For Townhouse\n" \
               f"Brick Type: {self.brick_type}"

    def bars(self):
        return f"Required Bars - For Townhouse\n" \
               f"Bars Name: {self.bars_name}\n" \
               f"Bars Type: {self.bars_quality}"


class Villa(House):
    """
    This class represents how villa type houses are built using
    different types of required materials and other additional
    materials.
    """
    def __init__(self, wood_name, wood_type, brick_type, bars_name, bars_quality,
                 paint_color, paint_primer, swimming_pool_size, water_fountain_type,
                 plant_type):
        self.wood_name = wood_name
        self.wood_type = wood_type
        self.brick_type = brick_type
        self.bars_name = bars_name
        self.bars_quality = bars_quality
        self.paint_color = paint_color
        self.paint_primer = paint_primer
        self.swimming_pool_size = swimming_pool_size
        self.water_fountain_type = water_fountain_type
        self.plant_type = plant_type

    def wood(self):
        return f"Required Wood - For Villa\n" \
               f"Wood Name: {self.wood_name}\n" \
               f"Wood Type: {self.wood_type}"

    def brick(self):
        return f"Required Brick - For Villa\n" \
               f"Brick Type: {self.brick_type}"

    def bars(self):
        return f"Required Bars - For Villa\n" \
               f"Bars Name: {self.bars_name}\n" \
               f"Bars Type: {self.bars_quality}"

    def paint(self):
        return f"Required Paint - For Villa\n" \
               f"Paint Color: {self.paint_color}\n" \
               f"Paint Primer: {self.paint_primer}"

    def garden(self):
        return f"Required Garden Construction Types - For Villa\n" \
               f"Plant Type: {self.plant_type}\n" \
               f"Water Fountain Type: {self.water_fountain_type}\n" \
               f"Swimming Pool Size: {self.swimming_pool_size}"


modular = Modular("Teak", "Indian", "Red Brick", "Twisted Iron Bars", "High Tension",
                  "Blue", "Paint Primer")
print(modular.wood())
print(modular.base())
print()
townhouse = Townhouse("Oak", "Cherrybark", "Burnt Clay", "High Carbon Iron Bars",
                      "Mid Tension")
print(townhouse.bars())
print(townhouse.base())
print()
villa = Villa("Sandalwood", "Indian", "Concrete", "High Carbon Iron Bars", "High Tension", "Yellow",
              "Paint Primer", "Rose", "Water Fountain", "20ft x 15ft x 10ft")
print(villa.garden())
print(villa.base())

house = House()
print(house)
