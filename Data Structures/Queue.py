class queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
        print(self.queue)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        popped = self.queue.pop(0)
        print(popped)
    def size(self):
        length = len(self.queue)
        print(length)

