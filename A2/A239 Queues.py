import timeit
class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0
      
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

queue_lengths = range(1000, 10000, 1000)

print("ImprovedQueue:")
for length in queue_lengths:
    queue = ImprovedQueue()
    for i in range(length):
        queue.enqueue(i)
    elapsed_time = timeit.timeit(lambda: queue.dequeue(), number=length)
    print(f"Queue length: {length}, elapsed time: {elapsed_time}")

print("\nQueue:")
for length in queue_lengths:
    queue = Queue()
    for i in range(length):
        queue.enqueue(i)
    elapsed_time = timeit.timeit(lambda: queue.dequeue(), number=length)
    print(f"Queue length: {length}, elapsed time: {elapsed_time}")
