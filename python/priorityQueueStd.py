#!/usr/bin/python

from __future__ import print_function
'''pip install sortedcontainers'''
'''http://www.grantjenks.com/docs/sortedcontainers/index.html'''
from sortedcontainers import SortedDict
import random
import sys


class PriorityQueue:
    def __init__(self):
        self.__buckets__ = SortedDict()
        return

    def enqueue(self, priority, value):
        bucket = self.__buckets__.setdefault(priority, [])
        bucket.append(value)
        return

    def dequeue(self):
        if len(self.__buckets__) > 0:
            (priority, bucket) = self.__buckets__.peekitem(0)
            value = bucket[0]
            if len(bucket) > 1:
                self.__buckets__[priority] = bucket[1:]
            else:
                del self.__buckets__[priority]
            return (priority, value)
        else:
            return None

    def clear(self):
        self.__buckets__.clear()
        return

    def size(self):
        total = 0
        for bucket in self.__buckets__.values():
            total += len(bucket)

        return total

    def count(self, priority):
        return len(self.__buckets__[priority]) if priority in self.__buckets__ else 0


def main():
    count = random.randint(1, 16384)
    items = []

    for i in range(0, count):
        priority = random.randint(1, 16384)
        items.append((priority, i))

    queue = PriorityQueue()

    for item in items:
        queue.enqueue(*item)    # should expand item into priority, value

    counts = {}
    for item in items:
        priority = item[0]
        counts[priority] = counts.get(priority, 0) + 1

    for priority in counts:
        count = counts[priority]
        if count != queue.count(priority):
            print("Count of items, {0}, with priority {1} doesn't match queue.Count(), {2}".format(count, priority, queue.count(priority)), file=sys.stderr)

    previous = (0, 0)
    while queue.size() > 0:
        entry = queue.dequeue()
        if entry[0] < previous[0]:
            print('Priority of item {0} is less than previous item, {1}'.format(entry, previous), file=sys.stderr)
        elif entry[0] == previous[0]:
            if entry[1] < previous[1]:
                print('Value of item {0} is less than previous item, {1}'.format(entry, previous), file=sys.stderr)
            else:
                print(entry)    # all is good
        else:   # entry[0] > previous[0]
            print(entry)    # all is good

        previous = entry

    return

if __name__ == '__main__':
    main()
