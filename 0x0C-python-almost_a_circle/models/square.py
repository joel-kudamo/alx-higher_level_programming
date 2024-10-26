#!/usr/bin/python3
"""Define Square class implement Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class body
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization class props in constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ return width size
        """
        return self.width

    @size.setter
    def size(self, value):
        """module Square height and width
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Square class string
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)
