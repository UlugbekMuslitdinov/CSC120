# UNICORN

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # Add item to the back of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the front item from the queue
        return self.queue.pop(0)


def hot_potato(q, num):
    while len(q.queue) > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


def sumlist(alist):
    if len(alist) == 0:
        return 0
    if len(alist) == 1:
        return alist[0]
    else:
        return alist[0] + sumlist(alist[1:])
