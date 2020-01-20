from ArrayQueue import ArrayQueue
import sys
sys.path.append(sys.path[0] + '/../DataStructure')


def n_bonacci(n, k):
    addends = ArrayQueue()
    for i in range(n):
        addends.enqueue(1)
    curr_sum = n
    for i in range(k):
        to_remove = addends.dequeue()
        yield to_remove
        addends.enqueue(curr_sum)
        curr_sum = curr_sum * 2 - to_remove
