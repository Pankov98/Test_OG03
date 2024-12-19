import math


def calculate_radius_from_area(area):
    if area < 0:
        raise ValueError("Площадь не может быть отрицательной")

    radius = math.sqrt(area / math.pi)
    return radius