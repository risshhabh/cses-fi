# https://cses.fi/problemset/task/1068

a = int(input())
while a != 1:
    print(a, end=" ")
    if a % 2:
        a = a * 3 + 1
    else:
        a //= 2

print(1, end="")