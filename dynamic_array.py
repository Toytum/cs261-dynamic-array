# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Ethan Weikel

import numpy as nmp

class DynamicArray:

    def __init__(self):
        self.capacity = 10
        self.data = nmp.empty(self.capacity, dtype=nmp.object)
        self.next_index = 0

        self.capacity = 10
        self.value = 0
        return None
        
    def is_empty(self):
        return True

    def append(self, val):
        self.data[self.next_index] = val
        self.next_index += 1

    def __len__(self):
        return self.next_index

    def __getitem__(self, index):
        return self.data[index]
