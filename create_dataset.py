from merge_sort import merge_sort
from random import shuffle
import pickle
from time import time


times = []
ex_start = time()
while input() != '':
    pass

for i in range(1000, 100000, 10):
    if i % 10000 == 0:
        print(i)
    test_list = list(range(i))
    shuffle(test_list)
    # pickle.dump(test_list, open('dataset_lists_2', 'ab'))
    ti = time()
    for _ in range(10):
        merge_sort(test_list)
    ti = (time() - ti) / 10
    times.append((ti, i))

if times:
    with open('dataset_execution_times', 'wb') as f:
        for i in times:
            pickle.dump(i, f)
    times = []

print(time() - ex_start)

''' 
Example of unpacking tuples of Execution Time:

with open('dataset_execution_times', 'rb') as f:
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break
'''
