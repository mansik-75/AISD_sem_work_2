import pickle
import matplotlib.pyplot as plt

import pylab

time = []
number = []
with open('dataset_execution_times', 'rb') as f:
    while True:
        try:
            a = pickle.load(f)
            time.append(float(a[0]))
            number.append(float(int(a[1])))
        except EOFError:
            break

plt.figure()
pylab.plot(number, time)
ax = pylab.subplot()
ax.set_xlabel('Numbers of elements')
ax.set_ylabel('Time')
plt.savefig('result.png')
