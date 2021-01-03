import attr
from math import sin, cos, pi


@attr.s(frozen=True)
class Coordinate:
    x: int = attr.ib()
    y: int = attr.ib()

    def __add__(self, other: "Coordinate") -> "Coordinate":
        return self.__class__(x=self.x + other.x, y=self.y + other.y)

    def __mul__(self, other: int) -> "Coordinate":
        return self.__class__(x=self.x * other, y=self.y * other)

    def __rmul__(self, other: int) -> "Coordinate":
        return self.__class__(x=self.x * other, y=self.y * other)

    def rotate(self, degrees: int) -> "Coordinate":
        # Rotate about the origin by number of degrees, counterclockwise
        # Convert to radians
        rads = degrees * pi / 180
        return self.__class__(
            x=round(self.x * cos(rads) - self.y * sin(rads)),
            y=round(self.x * sin(rads) + self.y * cos(rads)),
        )
