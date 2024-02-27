#
# Basically Pascals Triangle in a grid form: https://en.wikipedia.org/wiki/Pascal%27s_triangle
#
# 2 x 2 Block Grid:
#
# 6 3 1
# 3 2 1
# 1 1 1
#
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1


# Create a pascal triangle
def create_pascal_triangle(size):
    triangle = [[1]]
    for n in range(2, size + 1):
        triangle.append([])

        for i in range(n):
            prev = triangle[n - 2]
            x = prev[i - 1] if i - 1 >= 0 else 0
            y = prev[i] if i < len(prev) else 0
            triangle[n - 1].append(x + y)
    return triangle


def lattic_paths(grid_size):
    last = create_pascal_triangle(grid_size * 2)[-1]
    return last[len(last) // 2 - 1] + last[len(last) // 2]


# 1685 function calls in 0.000 seconds
print(lattic_paths(20))
