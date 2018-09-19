def area_of_triangle(a, b, c):
    (x1, y1) = a
    (x2, y2) = b
    (x3, y3) = c
    return 1 / 2 * (x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3)


def border_points(first_coord, second_coord):
    count_border_points = 0
    (x1, y1) = first_coord
    (x2, y2) = second_coord
    if x1 == x2:
        count_border_points = abs(y2 - y1) - 1
    elif y1 == y2:
        count_border_points = abs(x2 - x1) - 1
    else:
        for x in range(abs((x1 - x2))):
            y = y1 + (y2 - y1) / (x2 - x1) * (x - x1)
            if y.is_integer():
                count_border_points += 1
        if count_border_points:
            count_border_points -= 1
    return count_border_points


def count_points(a, b, c):
    area = abs(area_of_triangle(a, b, c))
    amount_of_border_points = border_points(a, b) + border_points(b, c) + border_points(a, c) + 3
    amount_of_inner_points = area - amount_of_border_points / 2 + 1
    print(int(amount_of_border_points + amount_of_inner_points))
    return


count_points((0, 0), (1, 0), (0, 1))
count_points((0, 0), (2, 0), (0, 2))
count_points((-2, -5), (0, 0), (5, 2))
count_points((5, 2), (0, 0), (-2, -5))
count_points((5, 2), (-2, -5), (0, 0))
