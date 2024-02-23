#!/usr/bin/env python3 

"""
atds.py
This Python program is a library of Python-implementations of Abstract Data Structures for the Advanced Topics in CS at Polytechnic School
"""

__author__ = "Sharon Chou"
__version__ = "2024-02-15"

class Stack(object):
    """
    Uses lists to implement a class Stack. 
    """
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if len(self.stack)>0:
            return self.stack[-1] #returns last value in the list
        else:
            return None
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack)==0
    
    def __repr__(self):
        return str(self.stack)
    
class Queue(object):
    """
    Uses lists to implement a class Queue. 
    """
    def __init__(self):
        self.q = []
    
    def enqueue(self, item):
        self.q.append(item)
        
    def dequeue(self):
        return self.q.pop(0) #python automatically moves everything over when you do pop fn on list
    
    def peek(self):
        return self.q[0]
    
    def size(self):
        return len(self.q)
    
    def is_empty(self):
        return len(self.q) == 0
    
    def __repr__(self):
        return str(self.q)
    

class Deque(object):
    """
    Uses lists to implement class Deque
    """
    def __init__(self):
        self.deque = []
    
    def add_front(self, item):
        self.deque.insert(0, item)
    
    def add_rear(self, item):
        self.deque.append(item)
    
    def remove_front(self):
        return self.deque.pop(0)
    
    def remove_rear(self):
        return self.deque.pop()
    
    def size(self):
        return len(self.deque)
    
    def is_empty(self):
        return len(self.deque) == 0
    
    
def main():
    s = Stack()
    s.push("Hello")
    s.push("Goodbye")
    print(s.pop())
    print(s.peek())
    print(s.size())
    print(s.is_empty())
    print(s.pop())
    print(s.is_empty())

if __name__ == "__main__":
    main()
