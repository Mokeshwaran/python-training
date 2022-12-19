from logger import logger
from typing import Self
from exceptions import CelestialBodyException
from util import is_valid_name, is_valid_number, is_valid_cluster_name
from enum import Enum
from math import pi

celestial_bodies = {}


class BodyType(Enum):
    """
    This class is an enum class which contains different types of celestial bodies
    in space.
    """
    ASTEROID = '1'
    GAS_GIANT = '2'
    ICE_GIANT = '3'
    PLANET = '4'


class CelestialBody:
    """
    This class contains the celestial bodies attributes and methods,
    Celestial Bodies are bodies or planets that are found in the space.
    """

    def __init__(self: Self, title: str = 'title',
                 body_type: str = 'body_type', diameter: int = 0, mass: int = 'mass',
                 angular_velocity: int = 0, linear_velocity: int = 0, distance: int = 0,
                 satellites: int = 0, cluster_name: str = 'cluster_name',
                 surface_temperature: int = 0, albedo: int = 0, gravity: int = 0,
                 is_deleted: int = 0):
        self.__title = title
        self.__body_type = body_type
        self.__diameter = diameter
        self.__mass = mass
        self.__angular_velocity = angular_velocity
        self.__linear_velocity = linear_velocity
        self.__distance = distance
        self.__satellites = satellites
        self.__cluster_name = cluster_name
        self.__surface_temperature = surface_temperature
        self.__albedo = albedo
        self.__gravity = gravity
        self.is_deleted = is_deleted

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def body_type(self):
        return self.__body_type

    @body_type.setter
    def body_type(self, body_type):
        self.__body_type = body_type

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter):
        self.__diameter = diameter

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        self.__mass = mass

    @property
    def angular_velocity(self):
        return self.__angular_velocity

    @angular_velocity.setter
    def angular_velocity(self, angular_velocity):
        self.__angular_velocity = angular_velocity

    @property
    def linear_velocity(self):
        return self.__linear_velocity

    @linear_velocity.setter
    def linear_velocity(self, linear_velocity):
        self.__linear_velocity = linear_velocity

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance):
        self.__distance = distance

    @property
    def satellites(self):
        return self.__satellites

    @satellites.setter
    def satellites(self, satellites):
        self.__satellites = satellites

    @property
    def cluster_name(self):
        return self.__cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        self.__cluster_name = cluster_name

    @property
    def surface_temperature(self):
        return self.__surface_temperature

    @surface_temperature.setter
    def surface_temperature(self, surface_temperature):
        self.__surface_temperature = surface_temperature

    @property
    def albedo(self):
        return self.__albedo

    @albedo.setter
    def albedo(self, albedo):
        self.__albedo = albedo

    @property
    def gravity(self):
        return self.__gravity

    @gravity.setter
    def gravity(self, gravity):
        self.__gravity = gravity


def main():
    """
    This is the main method of the program.
    :return: None
    :raises CelestialBodyException:
    """

    def set_celestial_body(title: str = 'title', body_type: str = 'body_type',
                           diameter: int = 0, mass: int = 0, angular_velocity: int = 0,
                           linear_velocity: int = 0, distance: int = 0,
                           satellites: int = 0, cluster_name: str = 'cluster_name',
                           surface_temperature: int = 0, albedo: int = 0):
        """
        This method will add a celestial body from the given values.

        :param title: str title of the celestial body given by the user.
        :param body_type: str body type of the celestial body given by the user.
        :param diameter: int diameter of the celestial body given by the user.
        :param mass: int mass of the celestial body given by the user.

        :param angular_velocity: int angular velocity of the celestial
        body given by the user (Angular Velocity is the rotational
        speed of the celestial body).

        :param linear_velocity: int linear velocity of the celestial
        body given by the user (Linear Velocity is the orbital velocity
        (speed around another celestial body) of the celestial body)

        :param distance: int distance of the celestial body given by the user.
        :param satellites: int number of satellites of the celestial
        body given by the user (Satellites are moons surrounding the celestial body)

        :param cluster_name: str cluster name of the celestial body given by the user
        (Galactic Cluster is the collection of celestial bodies)

        :param surface_temperature: int surface temperature of the celestial
        body given by the user

        :param albedo: int albedo of the celestial body given by the user
        (Albedo is the light reflected back from a celestial body usually between 0 and 1)

        :return: None
        """
        celestial_body = CelestialBody()
        celestial_body.title = title
        celestial_body.body_type = body_type
        celestial_body.diameter = diameter
        celestial_body.mass = mass
        celestial_body.angular_velocity = angular_velocity
        celestial_body.linear_velocity = linear_velocity
        celestial_body.distance = distance
        celestial_body.satellites = satellites
        celestial_body.cluster_name = cluster_name
        celestial_body.surface_temperature = surface_temperature
        celestial_body.albedo = albedo
        celestial_body.gravity = calculate_gravity(mass, diameter)

        celestial_bodies[title] = celestial_body

    def get_celestial_body(title: str = 'title'):
        """
        This method will return a single celestial body from the given title.
        :param title: str title of the celestial body given by the user.
        :return: List of celestial body's attributes.
        :raise CelestialBodyException: when the given celestial body doesn't exist.
        """
        celestial_body = celestial_bodies.get(title)
        if celestial_body is None or celestial_body.is_deleted == 1:
            logger.warning(f"Celestial Body {title} Doesn't Exist")
            return {}
        celestial_body = celestial_bodies[title]
        return celestial_body.__dict__

    def get_celestial_bodies():
        """
        This method will print all the celestial bodies.
        :return: None
        """
        if celestial_bodies.items() is None:
            return {}
        for i, j in celestial_bodies.items():
            if j.is_deleted == 0:
                print(i, j.__dict__)

    def delete_celestial_body(title: str = 'title'):
        """
        This method will soft delete a celestial body from the given title.
        :param title: str title of the celestial body given by the user.
        :return: None
        :raises CelestialBodyException: when the given title doesn't exist.
        """
        if celestial_bodies.get(title) is None:
            logger.warning(f"Celestial Body {title} Doesn't Exist")
            raise CelestialBodyException(f"Celestial Body {title} Doesn't Exist")
        celestial_bodies.get(title).is_deleted = 1

    def update_celestial_body(title, field_value='0'):
        """
        This method will update an existing celestial body's attributes.
        :param title: str title of the celestial body given by the user.
        :param field_value: str defaults to '0'
        based on that the update will take place.
        :return: str with a success message.
        """
        celestial_body = celestial_bodies.get(title)
        old_title = celestial_body.title
        if celestial_body is None:
            raise CelestialBodyException(f"Celestial Body {title} Doesn't Exist")
        match field_value:
            case '1':
                title = validate_input('title', 'string')
                celestial_body.title = title
                celestial_bodies[title] = celestial_bodies.pop(old_title)
                return "Title Updated"

            case '2':
                print("1. Asteroid\n"
                      "2. Gas Giant\n"
                      "3. Ice Giant\n"
                      "4. Planet\n")
                body_type_value = validate_input('body type', 'body_type')
                body_type = BodyType(body_type_value).name
                celestial_body.body_type = body_type
                return "Body Type Updated"

            case '3':
                diameter = validate_input('diameter')
                celestial_body.diameter = diameter
                return "Diameter Updated"

            case '4':
                mass = validate_input('mass')
                celestial_body.mass = mass
                return "Mass Updated"

            case '5':
                angular_velocity = validate_input('angular velocity')
                celestial_body.angular_velocity = angular_velocity
                return "Angular Velocity Updated"

            case '6':
                linear_velocity = validate_input('linear velocity')
                celestial_body.linear_velocity = linear_velocity
                return "Linear Updated"

            case '7':
                distance = validate_input('distance')
                celestial_body.distance = distance
                return "Distance from earth Updated"

            case '8':
                satellites = validate_input('satellites')
                celestial_body.satellites = satellites
                return "Number of Satellites Updated"

            case '9':
                cluster_name = validate_input('cluster name', 'string')
                celestial_body.cluster_name = cluster_name
                return "Cluster Name Updated"

            case '10':
                surface_temperature = validate_input('surface temperature')
                celestial_body.surface_temperature = surface_temperature
                return "Surface Name Updated"

            case '11':
                albedo = validate_input('albedo')
                celestial_body.albedo = albedo
                return "Albedo Updated"

            case _:
                return "Invalid Value"

    def calculate_gravity(mass: float = 0, diameter: int = 1):
        """
        This method will calculate and returns the gravity of a celestial body.
        :param mass: float mass of the celestial body given by the user.
        :param diameter: int diameter of the celestial body given by the user.
        :return: gravity: int to the user
        """
        if diameter == 0:
            logger.error("Cannot Divide By Zero")
            raise CelestialBodyException("Cannot Divide By Zero")
        gravity = (6.67 * (10 ** -11) * mass) / (diameter / 2)
        return gravity

    def is_exist(title: str = 'title'):
        """
        This method will check if the given celestial body is already exist.
        :param title: str title of the celestial body given by the user.
        :return: Boolean True
        """
        if celestial_bodies.get(title) is not None:
            logger.warning(f"Celestial Body {title} Already Exists")
            return True
        return False

    def compare_celestial_bodies(first_title: str = 'first_title',
                                 second_title: str = 'second_title'):
        """
        This method will return two celestial bodies to compare.
        :param first_title: str title of the celestial body given by the user.
        :param second_title: str title of the celestial body given by the user.
        :return: None
        :raises CelestialBodyException: when the specified title doesn't exist.
        """
        if celestial_bodies.get(first_title) is None:
            logger.warning(f"Celestial Body {first_title} Doesn't Exist")
            raise CelestialBodyException(f"Celestial Body {first_title} Doesn't Exist")
        if celestial_bodies.get(second_title) is None:
            logger.warning(f"Celestial Body {second_title} Doesn't Exist")
            raise CelestialBodyException(f"Celestial Body {second_title} Doesn't Exist")

        for i in range(len(celestial_bodies.get(first_title)) - 1):
            print(celestial_bodies.get(first_title)[i],
                  celestial_bodies.get(second_title)[i])

    def calculate_rotation(title):
        """
        This method will calculate the one period of rotation of a celestial body.
        :param title: str celestial body title given by the user
        :return: time_period: float calculated from the diameter and
        angular velocity of the celestial body
        """
        body = celestial_bodies.get(title)
        if body is None:
            raise CelestialBodyException(f"Celestial Body {title} Doesn't Exist")
        angular_velocity = int(body[3].split(" ")[-1])
        diameter = int(body[1].split(" ")[-1])
        if angular_velocity <= 0 or diameter <= 0:
            raise CelestialBodyException("Cannot Divide By Zero")
        time_period = 2 * pi * (diameter / 2) / angular_velocity
        return time_period

    def calculate_rotation_earth_time(title):
        """
        This method will return the time period of a celestial body
        converted to earth's time.
        :param title: str title of the celestial body given by the user.
        :return: time_period: str converted to earth's time.
        """
        hours = calculate_rotation(title) / 3600
        minutes = (hours - int(hours)) * 60
        seconds = (minutes - int(minutes)) * 60
        return f"Rotation: {int(hours)}hr, {int(minutes)}m, {int(seconds)}s"

    def validate_input(user_input, d_type='int'):
        """
        This method will validate the input given by the user if wrong input is given
        then the method will run again else it'll return a value.
        :param user_input: str input given by the user even digits are strings.
        :param d_type: str input to specify the type of input.
        :return: user_input: after validation of the data.
        """
        saved = user_input
        user_input = input(f"Enter the {user_input} of the celestial body: ")
        if saved == 'title':
            if not is_valid_name(user_input):
                logger.warning(f"Not A Valid {saved}")
                user_input = validate_input(saved, d_type)
            if is_exist(user_input):
                raise CelestialBodyException(f"Celestial Body {title} Already Exists")
            return user_input
        elif d_type == 'int':
            if not is_valid_number(user_input):
                logger.warning(f"Not A Valid Number")
                user_input = validate_input(saved, d_type)
            return user_input
        elif user_input.isdigit() and d_type == 'body_type':
            if 4 < int(user_input) < 0:
                logger.warning(f"Not A Valid Body Type")
                user_input = validate_input(saved, d_type)
            return user_input
        else:
            if not is_valid_cluster_name(user_input):
                logger.warning("Not A Valid Cluster Name")
                user_input = validate_input(saved, d_type)
            return user_input

    def celestial_body_input():
        """
        This method will get the input from the user to create a celestial body.
        :return: None
        """
        title = validate_input('title', 'string')
        print("1. Asteroid\n"
              "2. Gas Giant\n"
              "3. Ice Giant\n"
              "4. Planet\n")
        body_type_value = validate_input('body type', 'body_type')
        body_type = BodyType(body_type_value).name
        diameter = validate_input('diameter')
        mass = validate_input('mass')
        angular_velocity = validate_input('angular velocity')
        linear_velocity = validate_input('linear velocity')
        distance = validate_input('distance')
        satellites = validate_input('satellites')
        cluster_name = validate_input('cluster name', 'string')
        surface_temperature = validate_input('surface temperature')
        albedo = validate_input('albedo')

        logger.info("Method Call: set_celestial_body")
        set_celestial_body(title, body_type, int(diameter), int(mass), int(angular_velocity), int(linear_velocity),
                           int(distance), int(satellites), cluster_name, int(surface_temperature), int(albedo))

    flag = True
    while flag:
        choice = input("1. Add a celestial body\n"
                       "2. View a celestial body\n"
                       "3. View all celestial bodies\n"
                       "4. Delete a celestial body\n"
                       "5. Update a celestial body\n"
                       "6. Compare two celestial bodies\n"
                       "7. Calculate time period\n"
                       "8. Calculate time period in earth hours\n"
                       "9. Exit\n"
                       "Enter your choice: ")

        match choice:
            case '1':
                logger.info("Method Call: celestial_body_input")
                celestial_body_input()

            case '2':
                title = input("Enter the celestial body's name: ")
                logger.info("Method Call: get_celestial_body")
                print(get_celestial_body(title))

            case '3':
                logger.info("Method Call: get_celestial_bodies")
                print(get_celestial_bodies())

            case '4':
                title = input("Enter the celestial body's name: ")
                logger.info("Method Call: delete_celestial_body")
                print(delete_celestial_body(title))

            case '5':
                title = input("Enter the celestial body's name: ")
                if is_exist(title):
                    field_value = input("1. Title\n"
                                        "2. Body Type\n"
                                        "3. Diameter\n"
                                        "4. Mass\n"
                                        "5. Angular Velocity\n"
                                        "6. Linear Velocity\n"
                                        "7. Distance From Earth\n"
                                        "8. Number Of Satellites\n"
                                        "9. Cluster Name\n"
                                        "10. Surface Temperature\n"
                                        "11. Albedo\n"
                                        "Enter Your Value: ")
                    logger.info("Method Call: update_celestial_body")
                    print(update_celestial_body(title, field_value))
                else:
                    print("Data Not Found")

            case '6':
                first_body = input("Enter a celestial body's name: ")
                second_body = input("Enter a celestial body's name: ")
                logger.info("Method Call: compare_celestial_bodies")
                compare_celestial_bodies(first_body, second_body)

            case '7':
                title = input("Enter the celestial body's name: ")
                print(calculate_rotation(title))

            case '8':
                title = input("Enter the celestial body's name: ")
                print(calculate_rotation_earth_time(title))

            case _:
                flag = False


if __name__ == '__main__':
    flag = True
    while flag:
        try:
            main()
            flag = False
        except Exception as exception:
            logger.error(exception)
            print(exception)
