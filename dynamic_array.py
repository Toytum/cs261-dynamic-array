# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Ethan Weikel

class DynamicArray:

    def __init__(self):

        self.capacity = 10
        self.value = 0
        return None
        
    def is_empty(self):
        return True

    def __len__(self):
        return 0

    def append(self,num):
        self.value = num

    def __getitem__(self,num):
        return self.value