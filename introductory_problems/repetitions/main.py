# https://cses.fi/problemset/task/1069

sequence = input()
longest = [0]
last = sequence[0] 

for l in sequence:
    if l == last:
        longest[-1] += 1
    else:
        longest.append(1)
    last = l

print(max(longest))