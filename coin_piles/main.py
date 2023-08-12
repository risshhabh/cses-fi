# https://cses.fi/problemset/task/1754

splint = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    a, b = splint()
    if a == 0 and b == 0:
        print("YES")
    elif a == 0 or b == 0:
        print("NO")
    elif (a + b) % 3 or not 0.5 <= a / b <= 2:
        print("NO")
    else:
        print("YES")