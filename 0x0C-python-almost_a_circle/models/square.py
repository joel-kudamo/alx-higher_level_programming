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
