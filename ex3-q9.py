import numpy as np
import matplotlib.pyplot as plt

def chart(filename):
    x = np.genfromtxt(filename)

    max_index = np.argmax(x)
    max_x = x[max_index]

    plt.figure(figsize=(8, 6))
    plt.plot(x, color='blue')
    plt.scatter(max_index, max_x, color='red', marker='o', label='Maximum')
  
    plt.grid(True, linestyle='--', color='gray', alpha=0.7)
    plt.legend()

    plt.savefig('result.png', format='png')

    plt.show()

chart('2016-07-11_ipm_data.txt')
