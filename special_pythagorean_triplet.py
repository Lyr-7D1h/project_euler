def product_pythagorean_triplet(sum_triplet):
    for a in range(1, sum_triplet):
        for b in range(a, sum_triplet // 2):
            c = (a ** 2 + b ** 2) ** 0.5
            if c % 1 == 0:
                if a + b + c == sum_triplet:
                    return a * b * c


# 5 function calls in 0.049 seconds
print(product_pythagorean_triplet(1000))
