# https://cses.fi/problemset/task/1071

splint = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    y, x = splint()
    layer = max(x, y)  # max(layer) == layer ** 2
    print((layer ** 2 + (layer - 1) ** 2 + 1) // 2 + (x - y) * (-1 if not layer % 2 else 1))

"""
Diagonal = layer ** 2 + (layer - 1) ** 2
Offset = x - y but negate if even
"""