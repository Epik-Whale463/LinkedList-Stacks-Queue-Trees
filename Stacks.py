class FixedSizeStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity  # Create an empty list with the specified capacity
        self.size = 0  # Current size of the stack

    

    def push(self, item):
        if self.is_full():
            print("Stack is full. Cannot push element.")
            return
        self.stack[self.size] = item
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop element.")
            return None
        self.size -= 1
        popped_item = self.stack[self.size]
        self.stack[self.size] = None  # Remove the reference to the popped item
        return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek element.")
            return None
        return self.stack[self.size - 1]

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        for i in range(self.size - 1, -1, -1):
            print(self.stack[i])

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity


