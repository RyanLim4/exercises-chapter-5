"""Implements a deque."""


class Deque:
    """Implements a deque with a ring buffer."""

    def __init__(self, n):
        """Construct deque."""
        self.ring = [None] * n
        self.start = 0
        self.end = 0
        self.size = n

    def append(self, x):
        """Append x to end of deque."""
        self.ring[self.end] = x
        self.end += 1
        self.end %= self.size

    def appendleft(self, x):
        """Append x to the start of deque."""
        self.start -= 1
        self.start %= self.size
        self.ring[self.start] = x

    def pop(self):
        """Remove the last item in the Deque and return it."""
        self.end -= 1
        self.end %= self.size
        removed = self.ring[self.end]
        self.ring[self.end] = None
        return removed

    def popleft(self):
        """Remove the first item in the Deque and return it."""
        removed = self.ring[self.start]
        self.ring[self.start] = None
        self.start += 1
        self.start %= self.size
        return removed

    def peek(self):
        """Return the last item in the Deque without returning it."""
        return self.ring[(self.end-1) % self.size]

    def peekleft(self):
        """Return the first item in the Deque without returning it."""
        return self.ring[self.start]

    def __len__(self):
        """Return number of items currently in the deque."""
        return sum(x is not None for x in self.ring)

    def __iter__(self):
        """Perform iterator protocol."""
        return DequeIterator(self)


class DequeIterator:
    """Iterator class for Deque."""

    def __init__(self, deque):
        """Construct DequeIterator."""
        self.ring = deque.ring
        self.start = deque.start
        self.end = (deque.end - 1) % deque.size
        self.size = deque.size
        self.count = 0

    def __iter__(self):
        """Return Iterable."""
        return self

    def __next__(self):
        """Iterate step."""
        if self.ring[self.start] is None or self.count >= self.size:
            raise StopIteration
        else:
            next = self.start
            self.start += 1
            self.start = self.start % self.size
            self.count += 1
            return self.ring[next]
