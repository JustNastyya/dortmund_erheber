from random import choices

# 1 - pop
data = [
    [1, 27],
    [0, 25],
    [0, 26],
    [0, 21],
    [1, 29],
    [1, 20],
    [1, 21],
    [1, 22],
    [0, 20],
    [1, 24],
    [0, 28],
    [0, 23],
]

## e

iterations = 1000

sample_n = choices(data, k=iterations)

pop_sum = sum([a[0] for a in sample_n])
age_sum = sum([a[1] for a in sample_n])

pop_anteil = pop_sum / iterations
age_avg = age_sum / iterations

pop_sd = 1 / (iterations - 1) * sum([(a[0] - pop_anteil) ** 2 for a in sample_n])
# 0.2502
age_sd = 1 / (iterations - 1) * sum([(a[1] - age_avg) ** 2 for a in sample_n])
# 9.248
