from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.popleft()

    def search(self, index):
        if index < 0:
            raise IndexError('deque index out of range')
        return self._data[index]

    def is_empty(self):
        return not len(self._data)
