# https://cses.fi/problemset/task/1072

n = int(input())

for k in range(1, n + 1):
    K = k ** 2
    print((
          (K - 9) * (k - 4) ** 2 # middle
        + 4 * (K - 3)            # corners
        + 8 * (K - 4)            # corner sides
        + 4 * (k - 4) * (K - 5)  # sides
        + 4 * (K - 5)            # L2 corners
        + 4 * (k - 4) * (K - 7)  # L2 sides
    ) // 2)                      # overcounting XY = YX

"""
This simplifies as (k - 1)(k + 4)(k^2 - 3k + 4) / 2
"""