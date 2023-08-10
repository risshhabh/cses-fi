# https://cses.fi/problemset/task/1070

n = int(input())
print(f"{' '.join(list(map(str, range(2, n + 1, 2))))} {' '.join(list(map(str, range(1, n + 1, 2))))}" if n > 3 else "NO SOLUTION" if n != 1 else 1)