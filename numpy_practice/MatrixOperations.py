import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"A*B:\n{A*B}")

A = np.arange(1, 25)
A = A.reshape(2, 3, 4)
B = np.arange(1, 17)
B = B.reshape(2, 4, 2)

print(f"\nA:\n{A}\nB:{B}")

C = np.multiply(A, B)
print(f"\nC:{C}")
