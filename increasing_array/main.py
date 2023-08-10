# https://cses.fi/problemset/task/1094

splint = lambda : list(map(int, input().split()))

n = int(input())
x = splint()
last = x[0]
out = 0

for i in range(1, n):
    if x[i] < last:
        out += last - x[i]
        x[i] = last
    else:
        last = x[i]

print(out)