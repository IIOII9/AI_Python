import numpy as np

a = np.arange(1, 7)
a = a.reshape(2, 3)
b = np.array([10, 20, 30])
print(f"\n a:\n{a}\nb:\n{b}")
print(f"\n a+b:\n{a+b}")
