# https://cses.fi/problemset/task/1092

n = int(input())

y = n * (n + 1) // 2
if y % 2:
    print("NO")

elif not n % 2:
    print(f"YES\n{n // 2}")
    print(*range(1, n // 4 + 1) , *range(3 * n // 4 + 1, n + 1)) # q1, q4
    print(n // 2)
    print(*range(n // 4 + 1, 3 * n // 4 + 1)) # q2, q3

else:
    print("YES")
    print(n // 2 + 1)
    print(*range(1, n, 4), *range(2, n, 4))
    print(n // 2)
    print(*range(3, n, 4), *range(4, n, 4), n)