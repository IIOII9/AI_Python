import time

import numpy as np


def testnumpy():
    a = np.random.rand(10_000_000)
    b = np.random.rand(10_000_000)
    start = time.time()
    c = a + b
    print("\n向量化耗时：", time.time() - start)

    # 对比循环
    start = time.time()
    c_loop = np.zeros_like(a)
    for i in range(len(a)):
        c_loop[i] = a[i] + b[i]
    print("\n循环耗时：", time.time() - start)


if __name__ == "__main__":
    testnumpy()
