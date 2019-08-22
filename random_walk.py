from matplotlib import pyplot as plt
import random
max = 100000
x = [i for i in range(max)]

y = [0]

for i in range(1, max):
    y.append(y[i-1]  + random.randint(-1,1)) 

plt.plot(x, y)
plt.show()
