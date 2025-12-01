def total_sum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print(total_sum(5, 10))
print(total_sum(1, 2, 3, 4, 5))
