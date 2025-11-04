import numpy as np

a = np.arange(10)
print(f"\nArray is [{a}], a[-1]:{a[-1]}")
i = np.array([0, 2, 1, 2])
print(f"\n a[i]:{a[i]}")
print(a > 3)
print(a[a > 3])

c = np.random.rand(2, 3, 4)
print(f"\nc:{c}", f"\n c[0, ...]:{c[0,...]}, \nc[..., -1]:{c[..., -1]}")

a16 = np.arange(1, 17)
print(f"a16{a16}")
a16 = a16.reshape(4, 4)
print(f"a16{a16}")
