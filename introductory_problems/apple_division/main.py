# https://cses.fi/problemset/task/1623

splint = lambda : list(map(int, input().split()))

n = int(input())
p = sorted(splint(), reverse=True)
diff = p[0] - sum(p[1:])
done = False
for i in range(1, n):
    if abs(new := diff + 2 * p[i]) <= abs(diff):
        diff = new
    else:
        print(abs(diff))
        done = True
        break

if not done:
    print(abs(diff))