# https://cses.fi/problemset/task/1622

def combinations(i):
    n = len(i)

    if n == 1:
        return set(i)
    else:
        F, out = i[0], set()
        for C in combinations(i[1:]):
            for I in range(n+1):
                out.add(C[:I] + F + C[I:])
        return out

OUT = combinations(input())
print(len(OUT))
print("\n".join(sorted(list(OUT))))