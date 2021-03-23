def size(arr):
    """ Get the size of dynamic array """
    count = 0
    if arr is not None:
        for item in arr:
            if item is not None:
                count += 1
    return count


def from_list(lst):
    """ Construct a dynamic array from a list """
    arr = DynamicArray([])
    for i in range(len(lst)):
        arr.elements[i] = lst[i]
    return arr


def to_list(arr):
    """ Convert dynamic array to list """
    lst = []
    if arr is not None:
        for item in arr:
            lst.append(item)
    return lst


def find(arr, value):
    """ Find in the dynamic array whether there is an element with a value equal to 'value' """
    if arr is not None:
        for item in arr:
            if item is value:
                return True
    return False


def arr_filter(arr, is_even):
    """ Filter data structure by specific predicate """
    lst = []
    if arr is not None:
        for item in arr:
            if is_even:
                if (item % 2) == 0:
                    lst.append(item)
            else:
                if (item % 2) != 0:
                    lst.append(item)
    return DynamicArray(lst)


def arr_map(func, arr):
    """ Apply function to every item in array """
    lst = []
    for item in arr:
        lst.append(func(item))
    return DynamicArray(lst)


def arr_reduce(func, arr, initializer):
    """ Apply function of two arguments cumulatively to the items of array """
    it = iter(arr)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = func(value, element)
    return value


def append(arr, item):
    """ Append a new item to array """
    lst = to_list(arr)
    lst.append(item)
    return DynamicArray(lst)


def remove(arr, value):
    """ Remove an item whose value equal to 'value' from array """
    lst = []
    for i in range(size(arr)):
        if arr.elements[i] is not value:
            lst.append(arr.elements[i])
    return DynamicArray(lst)


def reverse(arr):
    """ Reverse the dynamic array """
    if arr is None:
        return None
    else:
        lst = []
        for i in range(size(arr) - 1, -1, -1):
            lst.append(arr.elements[i])
        return lst


def mempty():
    return None


def mconcat(a, b):
    """ Concatenate two arrays a and b """
    l1 = to_list(a)
    l2 = to_list(b)
    return DynamicArray(l1 + l2)


def iterator(arr):
    length = size(arr)
    lst = arr
    index = 0

    def foo():
        nonlocal lst
        nonlocal length
        nonlocal index
        if (index >= length) or (lst is None):
            raise StopIteration
        temp = lst.elements[index]
        index = index + 1
        return temp

    return foo


class DynamicArray(object):
    def __init__(self, lst=[]):
        self.elements = [None for i in range(100)]
        for i in range(len(lst)):
            self.elements[i] = lst[i]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.elements[self.index] is not None:
            x = self.elements[self.index]
            self.index += 1
            return x
        else:
            raise StopIteration

    def __eq__(self, other):
        if (other is None) or (size(other) != size(self)) or (type(other) != type(self)):
            return False
        for i in range(size(other)):
            if self.elements[i] != other.elements[i]:
                return False
        return True