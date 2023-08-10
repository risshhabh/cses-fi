# https://cses.fi/problemset/task/1083

print((n := int(input())) * (n + 1) / 2 - sum(list(map(int, input().split()))))