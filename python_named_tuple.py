from collections import namedtuple


role = ["Protagonist", "Antagonist", "SecondaryRole", "GuestAppearance", "SupportRole"]
# When above list contains a space between words then it raises
# ValueError: Type names and field names must be valid identifiers: 'Secondary Role'
cast = namedtuple("Movie", (i for i in role),
                  defaults=['proto', 'anto', 'secr', 'ga', 'sr'])
# Last value gets placed as default value
characters = cast("Mokeshwaran", "Yukendiran", "Dhanesh", "Harini", "Monisha")
print(characters)

role = ["Protagonist", "Antagonist", cast, "_GuestAppearance", "Protagonist"]
movie_characters = namedtuple("Movie", role, rename=True)
# With rename="False"
# ValueError: Type names and field names must be valid identifiers:
# "<class '__main__.Movie'>"
characters = movie_characters("Mokeshwaran", "Yukendiran", "Dhanesh", "Harini", "Monisha")
print(characters)

role = ["Protagonist", "Antagonist", cast, "_GuestAppearance", "Protagonist"]
movie_characters = namedtuple("Series", role, rename=True, module='Mokeshwaran')
# With rename="False"
# ValueError: Type names and field names must be valid identifiers:
# "<class '__main__.Movie'>"
characters = movie_characters("Mokeshwaran", "Yukendiran", "Dhanesh", "Harini", "Monisha")
print(characters)
print(characters.__module__)  # Default value: __main__

# We cannot use whitespaced values like "Ser ies"
# ValueError: Type names and field names must be valid identifiers: 'Ser ies'
