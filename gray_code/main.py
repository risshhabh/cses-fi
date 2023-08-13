# https://cses.fi/problemset/task/2205

n = int(input())

def gray_r(n):
    if n == 1:
        return [[0], [1]]
    else:
        L = 2 ** n
        A = gray_r(n - 1)
        A.extend(reversed(A))

        mult = 10 ** (n - 1)
        for i in range(L // 2, L):
            A[i] = list(map(lambda x : x + mult, A[i]))

        return A

for l in gray_r(n):
    print("\n".join(list(map(lambda p : str(p).zfill(n), l))))
