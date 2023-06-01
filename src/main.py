import logging
import math
from random import random

from tqdm import trange

from camera import Camera
from color import write_color
from hittable import HitRecord, Hittable
from hittable_list import HittableList
from ray import Ray
from sphere import Sphere
from vec3 import Vec3, random_in_unit_sphere, random_unit_vector, unit_vector

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def ray_color(r: Ray, world: Hittable, depth: int) -> Vec3:
    rec = HitRecord()

    if depth <= 0:
        return Vec3(0, 0, 0)

    is_hit, rec = world.hit(r, 0.001, math.inf, rec)
    if is_hit:
        target = rec.p + rec.normal + random_unit_vector()
        return 0.5 * ray_color(Ray(rec.p, target - rec.p), world, depth - 1)

    unit_direction = unit_vector(r.direction)
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)


def main() -> None:
    # Image

    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    samples_per_pixel = 100
    max_depth = 50

    # World

    world = HittableList()
    world.objects.append(Sphere(Vec3(0, 0, -1), 0.5))
    world.objects.append(Sphere(Vec3(0, -100.5, -1), 100))

    # Camera

    cam = Camera()

    # Render

    with open("image.ppm", "w", encoding="utf-8") as fp:
        fp.write(f"P3\n{image_width} {image_height}\n255\n")

        for j in trange(image_height - 1, -1, -1):
            for i in range(image_width):
                pixel_color = Vec3(0, 0, 0)

                for _ in range(samples_per_pixel):
                    u = (i + random()) / (image_width - 1)
                    v = (j + random()) / (image_height - 1)
                    r = cam.get_ray(u, v)
                    pixel_color += ray_color(r, world, max_depth)

                write_color(fp, pixel_color, samples_per_pixel)

    print("\nDone.\n")


if __name__ == "__main__":
    main()
