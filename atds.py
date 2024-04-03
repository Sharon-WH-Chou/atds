#!/usr/bin/env python3 

"""
atds.py
This Python program is a library of Python-implementations of Abstract Data Structures for the Advanced Topics in CS at Polytechnic School
"""

__author__ = "Sharon Chou"
__version__ = "2024-04-03"

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

class Node(object):
    """Defines a node class to be used in an UnorderedList, coming soon."""
    def __init__(self, data):
        self.data = data
        self.next = None #not pointing to anything originally
    
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
    
    def set_next(self, next):
        self.next = next
    
    def get_next(self):
        return self.next
    
    def __repr__(self):
        return "Node[data=" + str(self.data) + ",next=" + str(self.next) + "]"
    
class UnorderedList(object):
    """Defines an unordered (unsorted) list of nodes.
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, data):
        """Inserts a new node at the beginning of
        the list
        """
        temp_node = Node(data)
        temp_node.set_next(self.head)
        self.head = temp_node

    def length(self):
        """Identifies the length of the list by
        going through the entire list. Painful!
        """
        node_count = 0
        current = self.head
        while current != None:
            current = current.get_next()
            node_count += 1
        return node_count 

    def search(self, data):
        """Returns True if the data is on the list.
        """
        current = self.head
        found = False
        while current != None and not found: 
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, data):
        """Removes multiple occurrences of data on the list, 
        which requires going through the entire list until
        you hit the end, or nothing if the data isn't on the list.
        """
        current = self.head
        previous = None
        while current != None and self.head != None:    # Have to search entire list
            if current.get_data() == data:              # need to remove it
                if previous == None:                    # we're at the head
                    self.head = current.get_next()
                    current = current.get_next()
                else:
                    previous.set_next(current.get_next())
                    current = current.get_next()
            else:                                       # pass on through
                previous = current
                current = current.get_next()

    def append(self, data):
        """Appends an item to the end of the list
        """
        temp = Node(data) 
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(temp)

    def index(self, data):
        """Returns the index of the first occurence of the data
        in the list.
        """
        if self.head == None:
            return None
        current = self.head
        index = 0
        while current != None and current.get_data() != data:
            current = current.get_next()
            index += 1
        if current == None:
            return None
        else:
            return index

    def insert(self, position, data):
        """Inserts the piece of data at the indicated position.
        """
        temp = Node(data)
        index = 0
        current = self.head
        previous = None
        while index < position:
            previous = current
            current = current.get_next()
            index += 1
        if index == 0:
            temp.set_next(current)
            self.head = temp
        else:
            previous.set_next(temp)
            temp.set_next(current)
            
    def pop(self, index=-1):
        """Removes item at position index, or at the end of the list
        (-1) if no index is indicated.
        """
        if self.head == None:
            return None      # Can't pop from empty list
        if index == -1:
            current = self.head
            previous = None
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            result = current.get_data()
            previous.set_next(None)
            return result
        elif index == 0:
            current = self.head
            result = current.get_data()
            self.head = current.get_next()
            return result
        else:       # returning from middle of list?
            current = self.head
            previous = None
            position = 0
            while position < index:
                previous = current
                current = current.get_next()
                position += 1
            result = current.get_data()
            previous.set_next(current.get_next())
            return result

    def __repr__(self):
        """Creates a representation of the list suitable for printing, debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result

class UnorderedListStack(object):
    """Implements a Stack using the UnorderedList class.
    """
    def __init__(self):
        self.ul = UnorderedList()

    def push(self, item):
        """Pushes an item onto the top of the stack"""
        self.ul.add(item)

    def pop(self):
        """Removes the item at the top of the stack and
        returns it.
        """
        return self.ul.pop(0)
    
    def peek(self):
        """Examines the item at the top of the stack
        and returns that value. Awkward: we don't have
        a way to look at data at the beginning of an
        Unordered List!"""
        value = self.ul.pop(0)
        self.ul.add(value)
        return value

    def size(self):
        return self.ul.length()

    def is_empty(self):
        return self.ul.is_empty()

class HashTable():
    """Describes a has table based on two lists, "slots" and "values", and describes putting and getting values onto that table. Hash function is the mod (%) function, and collisions are handled using linear probing"""
    ###############################

    def __init__(self, m):
        """Creates an empty hash table of the size m
        """
        self.size = m                       # remember, prime numbers are better
        self.slots = [None] * self.size     # a list of None keys
        self.data = [None] * self.size      # a list of None values

###############################

    def hash_function(self, key, size):
        """This helper method returns the value of the hash function, based on 
        the key and the size of the table.
        """
        return key % size

###############################

    def put(self, key, value):
        """Places a key-value pair in the hash table (different key, collision => put in next available slot), or replaces the current value if the key already exists in the table (same key, diff value => replace old value)
        """
        location = self.hash_function(key, self.size)
        if self.slots[location] == None: #nothing there
            self.slots[location] = key
            self.data[location] = value
        elif self.slots[location] == key: #something is there with the same key
            self.data[location] == value
        elif self.slots[location] != None: #something is there with a different key
            while self.slots[location] != None:
                location = location + 1
            self.slots[location] = key
            self.data[location] = value
        
            
###############################

    def get(self, key):
        """Tries to find a key-value pair in the hash table (and return the value), or returns
        None if no key is found.
        """
        location = self.hash_function(key, self.size)
        if self.slots[location] == key:
            return self.data[location]
        else:
            while self.slots[location] != None:
                if self.slots[location] == key:
                    return self.data[location]
                location = location + 1
        return None
        
###############################

    def __repr__(self):
        """Returns a string representation of the hash table, displayed 
        as two arrays.
        """
        return "Keys:   " + str(self.slots) + "\n" + "Values: " + str(self.data)
    pass
    
def main():
    tests_passed = 0
    print("\nTEST: Creating HashTable(11)...")
    try:
        h = HashTable(11)
        tests_passed += 1
        print("SUCCESS. Table created.")
    except:
        print("FAIL. Table not created.")

    print("\nTEST: Using put function to store key-value pairs in table...")
    try:
        h.put(1, "a")
        h.put(6, "e")
        h.put(9, "f")
        h.put(12, "b")
        h.put(23, "c")
        tests_passed += 1
        print("SUCCESS. .put() method called with 5 values.")
    except:
        print("FAIL. Problem with .put() method.")

    print("\nTEST: Trying to print the current state of table:")
    try:
        print(h)
        print("Should look something like:")
        print("Keys:   [None, 1, 12, 23, None, None, 6, None, None, 9, None]")
        print("Values: [None, 'a', 'b', 'c', None, None, 'e', None, None, 'f', None]")
        tests_passed += 1
    except:
        print("FAIL. Couldn't print using __str__ or __repr__")
        


    print("\nTEST: Looking for original hash in table..")
    try:
        result = h.get(9)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "f":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nTEST: Looking for collision in table..")
    try:
        result = h.get(23)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "c":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nTEST: Looking for original hash not in table..")
    try:
        result = h.get(14)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent value not found.")
        else:
            print("FAIL. Non-existent value found.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nTEST: Looking for collision not in table..")
    try:
        result = h.get(45)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent collision not found.")
        else:
            print("FAIL. Non-existent collision found.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nResults:")
    print(tests_passed,"/ 9 tests passed")

if __name__ == "__main__":
    main()
