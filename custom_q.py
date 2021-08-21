class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
class Queue: # FIFO
    def __init__(self):
        self.head = None
        self.tall = None
        
    def enqueue(self, data):   # enqueue -> Adds an item to the queue
        if self.tall is None and self.head is None:
            self.tail = self.head = Node(data, None)
            return
        
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node
        return
    
    def dequeue(self):  # dequeue aka double-ended queue, has the feature of adding and removing elements from either end
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next_node
        
        if self.head is None:
            self.tail = None
        return removed
        
        
        
        
        
        
        
        
        
        