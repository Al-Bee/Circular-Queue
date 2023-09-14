class CircularQueue:

    def __init__(self, capacity=8):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.back = capacity - 1
        self.count = 0

    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.capacity
    
    def enqueue(self, item):
        if not self.is_full():
            self.back = (self.back + 1) % self.capacity
            self.items.insert(self.back, item)
            self.count += 1
        else:
            raise IndexError("ERROR: The queue is full.")
        
    def dequeue(self):
        if self.count != 0:
            tmp = self.items[self.front]
            self.front = (self.front + 1) % self.capacity
            self.count -= 1
            return tmp
        else:
            raise IndexError("ERROR: The queue is empty.")
    
    def show_contents(self):
        return f"{str(self.items)}, front:{self.front}, back:{self.back}, count:{self.count}"
    
    def __str__(self):
        for i in range(self.count):
            print(self.items[self.back + i])
try:
    q1 = CircularQueue(3)
    q1.enqueue("A")
    print(q1)
    q1.enqueue("B")
    print(q1)
    q1.enqueue("C")
    print(q1)
    q1.enqueue("D")
    print(q1)
except IndexError as err:
    print(err)