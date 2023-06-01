def clamp(x: float, min_: float, max_: float) -> float:
    if x < min_:
        return min_
    if x > max_:
        return max_
    return x
