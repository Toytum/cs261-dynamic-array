# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Ethan Weikel

import numpy as nmp

class DynamicArray:

    def __init__(self):
        self.capacity = 10
        self.data = nmp.empty(self.capacity, dtype=nmp.object)
        self.next_index = 0
        
    def is_empty(self):
        if self.next_index == 0:
            return True
        return False

    def append(self, val):
        self.data[self.next_index] = val
        self.next_index += 1

    def __len__(self):
        return self.next_index

    def __getitem__(self, index):
        if -1 < index < self.next_index :
            return self.data[index]
        else:
            raise IndexError("index out of range")

    def clear(self):
        self.next_index = 0
    
    def pop(self):
        self.next_index -= 1
        return self.data[self.next_index]