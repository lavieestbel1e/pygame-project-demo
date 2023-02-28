def test_is_prime(cases):
    return all(is_prime(keys) == values for keys, values in cases)


test_data = [
    (2, True),
    (1, False),
    (10, False),
    (15, False),
    (5, True),
    (103, True),
]

result = test_is_prime(test_data)
print('YES' if result else 'NO')