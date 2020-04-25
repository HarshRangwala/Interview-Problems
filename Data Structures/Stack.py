class stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
        print(self.items)
    def pop(self):
        self.items.pop()
        print(self.items)
    def peek(self):
        print(self.items[len(self.items) - 1])
    def size(self):
        length = len(self.items)
        print(length)
