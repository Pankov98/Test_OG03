import math


def calculate_radius_from_area(area):
    if area < 0:
        raise ValueError("Площадь не может быть отрицательной")

    radius = math.sqrt(area / math.pi)
    return radius


def sum_of_interior_angles(n):
    if n < 3:
        raise ValueError("Многоугольник должен иметь как минимум 3 стороны")

    # Используем формулу для нахождения суммы внутренних углов
    sum_angles = (n - 2) * 180
    return sum_angles