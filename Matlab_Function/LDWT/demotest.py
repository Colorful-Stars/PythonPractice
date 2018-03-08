N = 5
import numpy as np
s = np.zeros(N)
# s = np.ones(5)

print(s)
N = N / 2
for ii in range(int(N)):
    s[ii] = ii
    s[ii + int(N)] = ii

print(s)