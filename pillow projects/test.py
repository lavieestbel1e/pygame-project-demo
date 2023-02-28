ints = list(map(int, input().split()))

_10 = [i for i in ints if i % 10 == 0]
_11 = [i for i in ints if i % 10 in (1, 9)]

print(*_10 if _10 else '', sep=': ')
print(*_11 if _11 else '', sep='; ')