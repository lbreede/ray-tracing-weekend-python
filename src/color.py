import math
from typing import TextIO

from rtweekend import clamp
from vec3 import Vec3


def write_color(fp: TextIO, color_pixel: Vec3, samples_per_pixel: int) -> None:
    r, g, b = list(color_pixel)

    scale = 1.0 / samples_per_pixel
    r = math.sqrt(scale * r)
    g = math.sqrt(scale * g)
    b = math.sqrt(scale * b)

    fp.write(
        f"{int(256 * clamp(r, 0.0, 0.999))} "
        f"{int(256 * clamp(g, 0.0, 0.999))} "
        f"{int(256 * clamp(b, 0.0, 0.999))}\n"
    )
