#!/usr/bin/python

from __future__ import print_function
import sqlite3
import random
import sys


class PriorityQueue:
    def __init__(self):
        self.__connection__ = sqlite3.connect(':memory:')
        self.__cursor__ = self.__connection__.cursor()
        self.__cursor__.execute('CREATE TABLE items (priority INT, value INT)')
        self.__cursor__.execute('CREATE INDEX priorities ON items(priority)')
        self.__connection__.commit()
        return

    def enqueue(self, priority, value):
        self.__cursor__.execute('INSERT INTO items VALUES (?, ?)', (priority, value))
        self.__connection__.commit()
        return

    def dequeue(self):
        item = self.__cursor__.execute('SELECT priority, value FROM items ORDER BY priority, ROWID ASC LIMIT 1').fetchone()
        if item is not None:
            self.__cursor__.execute('DELETE FROM items WHERE priority=? AND value=?', item)
            self.__connection__.commit()

        return item

    def clear(self):
        self.__cursor__.execute('DELETE * FROM items')
        self.__connection__.commit()
        return

    def size(self):
        total = self.__cursor__.execute('SELECT COUNT(*) FROM items').fetchone()[0]

        return total

    def count(self, priority):
        count = self.__cursor__.execute('SELECT COUNT(*) FROM items WHERE priority=?', [priority]).fetchone()[0]

        return count


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
