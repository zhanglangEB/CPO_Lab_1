def size(arr):
    """ Get the size of dynamic array """
    if arr is None:
        return 0
    else:
        return arr.length


def from_list(lst: list):
    """ Construct a dynamic array from a list """
    arr = DynamicArray([])
    while len(lst) > len(arr.elements):
        resize(arr, 2)
    for i in range(len(lst)):
        arr.elements[i] = lst[i]
    arr.length = len(lst)
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


def arr_filter(arr, is_even: bool):
    """ Filter data structure by specific predicate """
    lst = []
    if arr is not None:
        for item in arr:
            if item is not None:
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
        if item is not None:
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
        if element is not None:
            value = func(value, element)
    return value


def resize(arr, growth_factor: int):
    """ Resize the dynamic array according to growth factor"""
    temp = [None] * len(arr.elements) * growth_factor
    for i in range(size(arr)):
        temp[i] = arr.elements[i]
    arr.elements = temp


def append(arr, item):
    """ Append a new item to array """
    if size(arr) == len(arr.elements):
        resize(arr)
    arr.elements[size(arr)] = item
    arr.length += 1
    return arr


def remove(arr, value):
    """ Remove an item whose value equal to 'value' from array """
    lst = to_list(arr)
    lst.remove(value)
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


class DynamicArray(object):
    def __init__(self, lst=[]):
        self.length = len(lst)
        if self.length <= 100:
            self.elements = [None for i in range(100)]
        else:
            self.elements = [None for i in range(self.length + 100)]
        for i in range(len(lst)):
            self.elements[i] = lst[i]

    def __iter__(self):
        return Next(self)

    def __eq__(self, other):
        if (other is None) or (size(other) != size(self)) or (type(other) != type(self)):
            return False
        for i in range(size(other)):
            if self.elements[i] != other.elements[i]:
                return False
        return True


class Next:
    def __init__(self, dynamic_arr):
        self.elements = dynamic_arr.elements
        self.length = dynamic_arr.length
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.length:
            x = self.elements[self.index]
            self.index += 1
            return x
        else:
            raise StopIteration
