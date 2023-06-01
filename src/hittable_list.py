from typing import Optional

from hittable import HitRecord, Hittable
from ray import Ray


class HittableList:
    def __init__(self, objects: Optional[list[Hittable]] = None):
        self.objects = objects or []

    def hit(
        self, r: Ray, t_min: float, t_max: float, rec: HitRecord
    ) -> tuple[bool, HitRecord]:
        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = t_max

        for obj in self.objects:
            is_hit, temp_rec = obj.hit(
                r, t_min, closest_so_far, temp_rec
            )  # TODO: Make rec mutable and only return a bool.
            if is_hit:
                hit_anything = True
                closest_so_far = temp_rec.t
                rec = temp_rec
                # rec.t = temp_rec.t
                # rec.p = temp_rec.p
                # rec.normal = temp_rec.normal
                # rec.material = temp_rec.material

        return hit_anything, rec  # TODO: Make rec mutable and only return a bool.
