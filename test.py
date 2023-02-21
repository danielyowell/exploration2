import random

import numpy as np
import matplotlib.pyplot as plt

# number of elements (major) // rows?
m = 512

# number of elements (minor) // columns?
n = 9

Q = np.zeros((m, n))

for _ in range(500):
    Q[random.choice(range(512))][random.choice(range(9))] = 1

print(Q)

# matplotlib.pyplot.spy(Z, precision=0, marker=None, markersize=None, aspect='equal', origin='upper', **kwargs)
plt.spy(Q, precision=0, marker=None, markersize=None, aspect='auto', origin='upper')
plt.show()