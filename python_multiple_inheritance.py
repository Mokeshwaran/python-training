class Mother:
    """
    This class represents the Mother's attributes.
    """
    def __init__(self, mothers_name: str, mothers_age: int) -> None:
        self.mothers_name = mothers_name
        self.mothers_age = mothers_age

    def __str__(self) -> str:
        return f"Mother's Name: {self.mothers_name}\n" \
               f"Mother's Age: {self.mothers_age}\n"


class Father:
    """
    This class represents the Father's attributes.
    """
    def __init__(self, fathers_name: str, fathers_age: int) -> None:
        self.fathers_name = fathers_name
        self.fathers_age = fathers_age

    def __str__(self) -> str:
        return f"Father's Name: {self.fathers_name}\n" \
               f"Father's Age: {self.fathers_age}"


class Child(Mother, Father):
    """
    This class represents the Child's attributes.
    """
    def __init__(self, name: str, age: int, mothers_name: str, mothers_age: int,
                 fathers_name: str, fathers_age: int) -> None:
        Mother.__init__(self, mothers_name=mothers_name,
                        mothers_age=mothers_age)
        Father.__init__(self, fathers_name=fathers_name,
                        fathers_age=fathers_age)
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name}\n" \
               f"Age: {self.age}\n" \
               f"{Mother.__str__(self)}" \
               f"{Father.__str__(self)}"


child = Child("Child Moki", 23, "Mother Moki", 110, "Father Moki", 130)
print(child)


# I followed the older way from this
# https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way
