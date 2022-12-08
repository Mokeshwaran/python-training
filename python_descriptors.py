class Reptiles:
    def __init__(self, name, reptile_type='Reptile'):
        self.name = name
        self.reptile_type = reptile_type

    def __get__(self, instance, owner):
        return self.name, self.reptile_type

    def __set__(self, instance, name, reptile_type):
        self.name = name
        self.reptile_type = reptile_type.
