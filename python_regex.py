from exceptions import CelestialBodyException
from regex_values import is_valid_name, is_valid_number, is_valid_cluster_name
from enum import Enum
from typing import Optional


class BodyType(Enum):
    ASTEROID = '1'
    GAS_GIANT = '2'
    ICE_GIANT = '3'
    PLANET = '4'


class CelestialBody:
    celestial_bodies = {}

    def __init__(self, title: str = 'title',
                 body_type: str = 'body_type', diameter: int = 0, mass: int = 'mass',
                 angular_velocity: int = 0, linear_velocity: int = 0, distance: int = 0,
                 satellites: int = 0, cluster_name: str = 'cluster_name',
                 surface_temperature: int = 0, albedo: int = 0, gravity: int = 0):
        self.title = title
        self.body_type = body_type
        self.diameter = diameter
        self.mass = mass
        self.angular_velocity = angular_velocity
        self.linear_velocity = linear_velocity
        self.distance = distance
        self.satellites = satellites
        self.cluster_name = cluster_name
        self.surface_temperature = surface_temperature
        self.albedo = albedo
        self.gravity = gravity

    def set_celestial_body(self, title: str = 'title', body_type: str = 'body_type',
                           diameter: int = 0, mass: int = 0, angular_velocity: int = 0,
                           linear_velocity: int = 0, distance: int = 0,
                           satellites: int = 0, cluster_name: str = 'cluster_name',
                           surface_temperature: int = 0, albedo: int = 0,
                           gravity: int = 0):

        self.celestial_bodies[title] = [
            f"Body Type: {body_type}", f"Diameter: {diameter}",
            f"Mass: {mass}", f"angular Velocity: {angular_velocity}",
            f"linear Velocity: {linear_velocity}", f"Distance From Earth: {distance}",
            f"Number Of Satellites: {satellites}",
            f"Galaxy Cluster Name: {cluster_name}",
            f"Surface Temperature: {surface_temperature}",
            f"Albedo: {albedo}", f"Gravity: {gravity}"
        ]

    def get_celestial_body(self, title):
        if self.celestial_bodies.get(title) is None:
            raise CelestialBodyException(f"Celestial Body {title} Doesn't Exist")
        return self.celestial_bodies[title]

    def get_celestial_bodies(self):
        return self.celestial_bodies

    def delete_celestial_body(self, title):
        if self.celestial_bodies.get(title) is None:
            raise CelestialBodyException(f"Celestial Body {title} Doesn't Exist")
        self.celestial_bodies.pop(title)

    @staticmethod
    def calculate_gravity(mass, diameter):
        gravity = (6.67 * (10 ** -11) * mass) / (diameter / 2)
        return gravity

    def is_exist(self, title):
        if self.celestial_bodies.get(title) is not None:
            raise CelestialBodyException(f"Celestial Body {title} Already Exists")

    def compare_celestial_bodies(self, first_title, second_title):
        if self.celestial_bodies.get(first_title) is None:
            raise CelestialBodyException(f"Celestial Body {first_title} Doesn't Exist")
        if self.celestial_bodies.get(second_title) is None:
            raise CelestialBodyException(f"Celestial Body {second_title} Doesn't Exist")

        for i in range(len(self.celestial_bodies.get(first_title)) - 1):
            print(self.celestial_bodies.get(first_title)[i],
                  self.celestial_bodies.get(second_title)[i])


def main():
    celestial_body = CelestialBody()

    def celestial_body_input():
        title = input("Enter the title of the celestial body: ")
        if not is_valid_name(title):
            raise CelestialBodyException("Not A Valid Planet Name")
        celestial_body.is_exist(title)

        body_type_value = input("1. Asteroid\n"
                                "2. Gas Giant\n"
                                "3. Ice Giant\n"
                                "4. Planet\n"
                                "Enter the body type of the celestial body: ")
        if not is_valid_number(body_type_value):
            raise CelestialBodyException("Not A Valid Body Type")
        body_type = BodyType(body_type_value).name

        diameter = input("Enter the diameter of the celestial body: ")
        if not is_valid_number(diameter):
            raise CelestialBodyException("Not A Valid Diameter")

        mass = input("Enter the mass of the celestial body: ")
        if not is_valid_number(mass):
            raise CelestialBodyException("Not A Valid Mass")

        angular_velocity = \
            input("Enter the angular velocity of the celestial body: ")
        if not is_valid_number(angular_velocity):
            raise CelestialBodyException("Not A Valid Angular Velocity")

        linear_velocity = input("Enter the linear velocity of the celestial body: ")
        if not is_valid_number(linear_velocity):
            raise CelestialBodyException("Not A Valid Linear Velocity")

        distance = input("Enter the distance from earth of the celestial body: ")
        if not is_valid_number(distance):
            raise CelestialBodyException("Not A Valid Distance")

        satellites = input("Enter the number of satellites of the celestial body: ")
        if not is_valid_number(satellites):
            raise CelestialBodyException("Not A Valid Number Of Satellites")

        cluster_name = \
            input("Enter the galactic cluster name of the celestial body: ")
        if not is_valid_cluster_name(cluster_name):
            raise CelestialBodyException("Not A Valid Cluster Name")

        surface_temperature = \
            input("Enter the surface temperature of the celestial body: ")
        if not is_valid_number(surface_temperature):
            raise CelestialBodyException("Not A Valid Surface Temperature")

        albedo = input("Enter the albedo of the celestial body: ")
        if not is_valid_number(albedo):
            raise CelestialBodyException("Not A Valid Albedo")

        celestial_body.set_celestial_body(title, body_type, int(diameter),
                                          int(mass),
                                          int(angular_velocity),
                                          int(linear_velocity), int(distance),
                                          int(satellites), cluster_name,
                                          int(surface_temperature),
                                          int(albedo),
                                          celestial_body
                                          .calculate_gravity(int(mass), int(diameter)))

    flag = True
    while flag:
        choice = input("1. Add a celestial body\n"
                       "2. View a celestial body\n"
                       "3. View all celestial bodies\n"
                       "4. Delete a celestial body\n"
                       "5. Compare two celestial bodies\n"
                       "6. Exit\n"
                       "Enter your choice: ")

        match choice:
            case '1':
                celestial_body_input()

            case '2':
                title = input("Enter the celestial bodies name: ")
                print(celestial_body.get_celestial_body(title))

            case '3':
                print(celestial_body.get_celestial_bodies())

            case '4':
                title = input("Enter the celestial bodies name: ")
                print(celestial_body.delete_celestial_body(title))

            case '5':
                first_body = input("Enter a celestial bodies name: ")
                second_body = input("Enter a celestial bodies name: ")
                celestial_body.compare_celestial_bodies(first_body, second_body)

            case _:
                flag = False


if __name__ == '__main__':
    flag = True
    while flag:
        try:
            main()
            flag = False
        except Exception as exception:
            print(exception)
