#!/usr/bin/env python3
" Stacking Bars "
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

fruitT = fruit.transpose()
labels = ['apples', 'bananas', 'oranges', 'peaches']
lColors = ['#ffe5b4', '#ff8000', 'yellow', 'red']
ind = [1, 2, 3]
width = 0.5
val = []

for j in range(0, len(fruitT[0]) - 1):
    row = []
    for i in range(0, len(fruitT[j])):
        if i == 0:
            row.append(fruitT[j][i])
        else:
            row.append(row[i-1] + fruitT[j][i])
    val.append(row)

b1 = plt.bar(1,
             [val[0][3], val[0][2], val[0][1], val[0][0]],
             width,
             color=lColors)
b2 = plt.bar(2,
             [val[1][3], val[1][2], val[1][1], val[1][0]],
             width,
             color=lColors)
b3 = plt.bar(3,
             [val[2][3], val[2][2], val[2][1], val[2][0]],
             width,
             color=lColors)

plt.xticks(ind, ('Farrah', 'Fred', 'Felicia'))
plt.legend((b3[3], b2[2], b2[1], b1[0]), labels)
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.yticks(range(0, 90, 10))
plt.show()
