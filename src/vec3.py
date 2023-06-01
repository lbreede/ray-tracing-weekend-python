from __future__ import annotations

import math
import random


class Vec3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def length(self) -> float:
        return math.sqrt(self.length_squared())

    def length_squared(self) -> float:
        return self.x * self.x + self.y * self.y + self.z * self.z

    @staticmethod
    def random() -> Vec3:
        return Vec3(random.random(), random.random(), random.random())

    @staticmethod
    def random_range(min_: float, max_: float) -> Vec3:
        return Vec3(
            random.uniform(min_, max_),
            random.uniform(min_, max_),
            random.uniform(min_, max_),
        )

    @staticmethod
    def random_in_unit_sphere() -> Vec3:
        while True:
            p = Vec3.random_range(-1, 1)
            if p.length_squared() >= 1:
                continue
            return p

    def dot(self, other: Vec3) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: Vec3) -> Vec3:
        return Vec3(
            self.y * other.z - self.z * other.y,
            -(self.x * other.z - self.z * other.x),
            self.x * other.y - self.y * other.x,
        )

    def __neg__(self) -> Vec3:
        return Vec3(-self.x, -self.y, -self.z)

    def __add__(self, other: Vec3 | float | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (float, int)):
            return Vec3(self.x + other, self.y + other, self.z + other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: 'Vec3' and '{type(other)}'"
            )

    def __radd__(self, other: Vec3 | float | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (float, int)):
            return Vec3(self.x + other, self.y + other, self.z + other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: 'Vec3' and '{type(other)}'"
            )

    def __sub__(self, other: Vec3 | float | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (float, int)):
            return Vec3(self.x - other, self.y - other, self.z - other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for -: 'Vec3' and '{type(other)}'"
            )

    def __mul__(self, other: Vec3 | float | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        if isinstance(other, (float, int)):
            return Vec3(self.x * other, self.y * other, self.z * other)
        raise TypeError(
            f"unsupported operand type(s) for *: 'Vec3' and '{type(other)}'"
        )

    def __rmul__(self, other: Vec3 | float | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        if isinstance(other, (float, int)):
            return Vec3(self.x * other, self.y * other, self.z * other)

        raise TypeError(
            f"unsupported operand type(s) for *: 'Vec3' and '{type(other)}'"
        )

    def __truediv__(self, other: Vec3 | float | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        elif isinstance(other, (float, int)):
            return Vec3(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for /: 'Vec3' and '{type(other)}'"
            )

    def __floordiv__(self, other: Vec3 | float | int) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x // other.x, self.y // other.y, self.z // other.z)
        elif isinstance(other, (float, int)):
            return Vec3(self.x // other, self.y // other, self.z // other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for //: 'Vec3' and '{type(other)}'"
            )

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __repr__(self) -> str:
        return f"Vec3({self.x}, {self.y}, {self.z})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"


def dot(u: Vec3, v: Vec3) -> float:
    return u.x * v.x + u.y * v.y + u.z * v.z


def cross(u: Vec3, v: Vec3) -> Vec3:
    return Vec3(u.y * v.z - u.z * v.y, u.z * v.x - u.x * v.z, u.x * v.y - u.y * v.x)


def unit_vector(v: Vec3) -> Vec3:
    """Returns a unit vector of v.

    Args:
        v (Vec3): A vector.

    Returns:
        Vec3: A unit vector of v.

    """
    return v / v.length()


def random_in_unit_sphere() -> Vec3:
    while True:
        p = Vec3.random_range(-1, 1)
        if p.length_squared() >= 1:
            continue
        return p


def random_unit_vector() -> Vec3:
    return unit_vector(random_in_unit_sphere())


def random_vec3() -> Vec3:
    return Vec3(random.random(), random.random(), random.random())


def random_range(min_: float, max_: float) -> float:
    return min_ + (max_ - min_) * random.random()


def random_in_hemisphere(normal: Vec3) -> Vec3:
    in_unit_sphere = random_in_unit_sphere()
    if dot(in_unit_sphere, normal) > 0.0:
        return in_unit_sphere
    else:
        return -in_unit_sphere


def main() -> None:
    v = Vec3.random_in_unit_sphere()
    print(v)


if __name__ == "__main__":
    main()
