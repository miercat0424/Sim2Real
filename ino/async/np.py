import numpy as np

a = np.ones(3)
b = np.ones(3)
# c = np.arange(6,9)

a = np.vstack([a,b])
print(a)
print(a[-1][0])