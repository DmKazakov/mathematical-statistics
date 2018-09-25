import numpy as np
import matplotlib.pyplot as plt
import sys
import math

MAX_K_VALUE = 100
REPETITIONS_NUMBER = 500


def eval_exp_deviation():
    sample_set = np.random.exponential(theta, n)
    m = np.mean([x ** k for x in sample_set])
    return (theta - (m / math.factorial(k)) ** (1 / k)) ** 2


def eval_uniform_deviation():
    sample_set = np.random.uniform(0, theta, n)
    m = np.mean([x ** k for x in sample_set])
    return (theta - (m * (k + 1)) ** (1 / k)) ** 2


try:
    theta = float(input("Enter theta parameter: "))
except ValueError:
    sys.exit('Type of theta parameter must be float')
if theta < 0:
    sys.exit('Theta parameter must be positive.')
try:
    n = int(input("Enter sample set size: "))
except ValueError:
    sys.exit('Sample set size must be integer')
if n < 0:
    sys.exit('Sample set size must be positive.')

exp_st_deviation = []
uniform_st_deviation = []
for k in range(1, MAX_K_VALUE):
    exp_deviations = [eval_exp_deviation() for _ in range(REPETITIONS_NUMBER)]
    exp_st_deviation.append(np.mean(exp_deviations))
    uniform_deviations = [eval_uniform_deviation() for _ in range(REPETITIONS_NUMBER)]
    uniform_st_deviation.append(np.mean(uniform_deviations))

plt.subplot(1, 2, 1)
plt.plot([x for x in range(1, MAX_K_VALUE)], exp_st_deviation)
plt.ylabel('deviation')
plt.xlabel('k')
plt.title('exponential')

plt.subplot(1, 2, 2)
plt.plot([x for x in range(1, MAX_K_VALUE)], uniform_st_deviation)
plt.xlabel('k')
plt.title('uniform')

plt.show()
