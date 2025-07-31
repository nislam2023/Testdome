def find_roots(a, b, c):
    x = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 / a, (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 / a
    return x


print(find_roots(2, 10, 8))
