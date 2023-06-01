from vec3 import Vec3


class Ray:
    def __init__(self, origin: Vec3, direction: Vec3) -> None:
        self.origin = origin
        self.direction = direction

    def at(self, t: float) -> Vec3:
        """Returns the point at t along the ray

        Args:
            t (float): The distance along the ray

        Returns:
            Vec3: The point at t along the ray

        """
        return self.origin + t * self.direction

    def __repr__(self) -> str:
        return f"Ray({self.origin}, {self.direction})"

    def __str__(self) -> str:
        return f"Origin: {self.origin}, Direction: {self.direction}"
