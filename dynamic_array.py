# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Ethan Weikel

class DynamicArray:
    name = " "
    actualList = [None]
    capacity = 10
    r = range(0,10)
    for n in r:
        actualList.append(None)


    def __init__(self):
        return None

    def is_empty(self):
        return True

    def __len__(self):
        return 0
        
    def append(self,numb):

        pass

    def __getitem__(self, numb):
        return 42
    pass
