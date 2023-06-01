from dataclasses import dataclass
from typing import Protocol

from ray import Ray
from vec3 import Vec3, dot


class HitRecord:
    def __init__(
        self,
        p: Vec3 = Vec3(0, 0, 0),
        normal: Vec3 = Vec3(0, 0, 0),
        t: float = 0.0,
        front_face: bool = False,
    ) -> None:
        self.p = p
        self.normal = normal
        self.t = t
        self.front_face = front_face

    def set_face_normal(self, r: Ray, outward_normal: Vec3) -> None:
        self.front_face = dot(r.direction, outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal


class Hittable(Protocol):
    def hit(
        self, r: Ray, t_min: float, t_max: float, rec: HitRecord
    ) -> tuple[bool, HitRecord]:
        """Return whether the ray hits the object and the hit record.

        Args:
            r (Ray): The ray to check for a hit.
            t_min (float): The minimum value of t to consider.
            t_max (float): The maximum value of t to consider.
            rec (HitRecord): The hit record to be updated.

        Returns:
            HitResult: Whether the ray hits the object and the hit record.

        """
        ...
