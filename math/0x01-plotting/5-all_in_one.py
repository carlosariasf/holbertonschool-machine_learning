#!/usr/bin/env python3
" All in One "
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.rcParams.update({'axes.labelsize': 'x-small',
                     'axes.titlesize': 'x-small',
                     'legend.fontsize': 'x-small'})

plt.subplot(321)
plt.plot(y0, 'r')
plt.xlim(0, 10)

plt.subplot(322)
plt.scatter(x1, y1, c='m', s=9)
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')
plt.title('Men\'s Height vs Weight')

plt.subplot(323)
plt.plot(x2, y2)
plt.yscale('log')
plt.xlim(0, 28650)
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of C-14')

plt.subplot(324)
plt.plot(x3, y31, 'r--', label='C-14')
plt.plot(x3, y32, 'g', label='Ra-226')
plt.legend()
plt.xlim(0, 20000)
plt.ylim(0, 1)
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of Radioactive Elements')

plt.subplot(3, 2, (5, 6))
plt.hist(student_grades, bins=range(10, 110, 10), edgecolor='k')
plt.xticks(range(0, 110, 10))
plt.ylim(0, 30)
plt.xlim(0, 100)
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')

plt.tight_layout()
plt.suptitle('All in One')
plt.show()
