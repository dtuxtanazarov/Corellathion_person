import math

def pearson_correlation(x, y):
    if len(x) != len(y):
        raise ValueError("Ikkala ro'yxat bir xil uzunlikda bo'lishi kerak.")

    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    denominator_y = sum((y[i] - mean_y) ** 2 for i in range(n))

    denominator = math.sqrt(denominator_x * denominator_y)

    if denominator == 0:
        return 0  # Korrelyatsiya aniqlanmaydi

    r = numerator / denominator
    return r


# Misol:
x = [10, 20, 30, 40, 50]
y = [15, 25, 35, 45, 60]

r = pearson_correlation(x, y)
print(f"Pearson korrelyatsiyasi: {r:.4f}")
