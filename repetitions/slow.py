# https://cses.fi/problemset/task/1069
# Slow implement

import re

sequence = input()
A = max(re.split("T|C|G", sequence), key = len)
T = max(re.split("A|C|G", sequence), key = len)
C = max(re.split("T|A|G", sequence), key = len)
G = max(re.split("T|C|A", sequence), key = len)

print(len(max(A, T, C, G, key = len)))