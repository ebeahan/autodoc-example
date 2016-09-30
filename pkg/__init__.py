
NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"

class Pkg(object):
    """My Pkg class.

    My simple Pkg class.

    .. note::

        A useful note might appear here.

    """
    def __init__(self, direction, speed=30):
        """A really simple class.

        Args:
            direction (str): Pass in a direction.

        Kwargs:
            speed (int): The speed

        """
        self.direction = direction
        self.speed = speed

    def change_direction(new_direction):
        """Method to allow changing the class
        instance's direction attribute.

        :param new_direction: string
        """
        self.direction = new_direction

def foo(x, y):
    """.. function:: foo(value1, value2)

    Pass two values and return their sum.

    :param value1: integer
    :param value2: integer
    :rtype: integer
    """
    return x + y

