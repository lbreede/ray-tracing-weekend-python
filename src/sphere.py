import math

from hittable import HitRecord
from ray import Ray
from vec3 import Vec3


class Sphere:
    def __init__(self, center: Vec3, radius: float) -> None:
        self.center = center
        self.radius = radius

    def hit(
        self, r: Ray, t_min: float, t_max: float, rec: HitRecord
    ) -> tuple[bool, HitRecord]:
        oc = r.origin - self.center
        a = r.direction.length_squared()
        half_b = oc.dot(r.direction)
        c = oc.length_squared() - self.radius * self.radius

        discriminant = half_b * half_b - a * c
        if discriminant < 0:
            return False, rec
        sqrtd = math.sqrt(discriminant)

        # Find the nearest root that lies in the acceptable range.
        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False, rec

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)

        return True, rec  # TODO: Make rec mutable and only return a bool.
