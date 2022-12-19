class CelestialBodyException(Exception):
    def __init__(self, msg="Something Went Wrong"):
        self.msg = msg

    def __str__(self):
        return self.msg
