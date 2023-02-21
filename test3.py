import matplotlib.pyplot as plt
import numpy as np

a = np.random.random((16, 16))
#d=a.todense()
plt.imshow(a,interpolation='none',cmap='binary')
plt.colorbar()
plt.show()