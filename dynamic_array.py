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
        self.expand()
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
        if self.next_index != 0:
            self.next_index -= 1
            return self.data[self.next_index]
        else:
            raise IndexError("index out of range")

    def delete(self, index):
        if not index < self.next_index:
            raise IndexError("index out of range")
        else:
            while( index < self.next_index):
                self.data[index] = self.data[index + 1]
                index += 1
            self.next_index -= 1

    def insert(self, index, val):
            if not index <= self.next_index:
                raise IndexError("index out of range")
            else:
                self.expand()
                self.next_index += 1
                i = self.next_index
                while(i >= index):
                    self.expand()
                    self.data[i] = self.data[i-1]
                    i -= 1
                self.data[index] = val

    def is_full(self):
        if self.next_index == self.capacity:
            return True
        return False

    def expand(self):
        if self.is_full():
            expanded_capacity = self.capacity * 2
            expanded_array = nmp.empty(expanded_capacity, dtype = nmp.object)
            new_index = 0

            while(new_index < self.next_index):
                expanded_array[new_index] = self.data[new_index]
                new_index += 1
            self.data = expanded_array
            self.capacity = expanded_capacity

    def max(self):
        i = 0
        max_val = 0
        if self.is_empty():
            return None
        else:
            while(i < self.next_index):
                if self.data[i] > max_val:
                    max_val = self.data[i]
                i += 1
        
        return max_val

    def min(self):
        i = 0
        min_val = self.data[0]
        if self.is_empty():
            return None
        else:
            while(i < self.next_index):
                if self.data[i] < min_val:
                    min_val = self.data[i]
                i += 1

        return min_val
    
    def sum(self):
        i = 0
        sum_val = 0
        if self.is_empty():
            return None
        else:
            while(i < self.next_index):
                sum_val += self.data[i]
                i += 1

        return sum_val

    def linear_search(self, target):
        i = 0
        while(i < self.next_index):
            if self.data[i] == target:
                return i
            else:
                i +=1
    
    # def binary_search(self, low = 0, high= 0, target):
    #     sort(self.data)
    #     low = self.data[0]
    #     high = self.data[self.next_index-1]
    #     mid = (high + low) // 2

    #     if high >= low:
    #         if self.data[mid] == target:
    #             return mid
    #         elif self.data[mid] > target:
    #             return binary_search(low, mid-1, target)
    #         else self.data[mid] < target:
    #             return binary_search(mid+1, high, target)
    #     else:
    #         return None
        
