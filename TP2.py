def max_of_two(x: float, y: float) -> float:
    biggest: float
    if x >= y:
        biggest = x
    else:
        biggest = y
    return biggest


def max_of_three(x: float, y: float, z: float) -> float:
    biggest: float = x
    if x > y and x > z:
        biggest = x
    elif y > x and y > z:
        biggest = y
    elif z > x and z > y:
        biggest = z
    return biggest


def leap_year(year: int) -> None:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
