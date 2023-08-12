# https://cses.fi/problemset/task/1618

n = int(input())
out = 0
for i in range(1, 13):
    out += n // (5 ** i)

print(out)