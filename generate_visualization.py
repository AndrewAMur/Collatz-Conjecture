import matplotlib.pyplot as plt
import numpy as np

def collatz_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

num_integers = 1000

x = np.arange(1, num_integers + 1)
y = np.array([collatz_length(i) for i in x])

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Collatz Conjecture Sequence Lengths')
plt.xlabel('Starting Number')
plt.ylabel('Sequence Length')
plt.grid(True)
plt.show()
