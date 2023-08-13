# https://cses.fi/problemset/task/1755

s = sorted(input())
d: dict = {}

for l in s:
    try:
        d[l] += 1
    except KeyError:
        d[l] = 1

if sum(map(lambda i : i % 2, d.values())) > 1:
    print("NO SOLUTION")
else:
    out = ''
    center = ''
    for k, v in d.items():
        if not v % 2:
            out += k * (v // 2)
        else:
            center = k
            out += k * (v // 2)
    print(out + center + out[::-1])