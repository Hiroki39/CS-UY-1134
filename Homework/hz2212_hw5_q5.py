import sys
sys.path.append(sys.path[0] + '/../DataStructure')
import copy
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack


def permutations(lst):
    elem_stack = ArrayStack()
    p_collection = ArrayQueue()
    for elem in lst:
        elem_stack.push(elem)
    for i in range(len(elem_stack)):
        new_elem = elem_stack.pop()
        if p_collection.is_empty():
            p_collection.enqueue([new_elem])
        else:
            for j in range(len(p_collection)):
                old_p = p_collection.dequeue()
                for k in range(len(old_p) + 1):
                    new_p = copy.copy(old_p)
                    new_p.insert(k, new_elem)
                    p_collection.enqueue(new_p)
    return [p_collection.dequeue() for i in range(len(p_collection))]
