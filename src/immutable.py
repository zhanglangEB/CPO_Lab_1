class DynamicArray(object):
    def __init__(self, lst=[]):
        if not isinstance(lst, list):
            raise TypeError('The type of {} object is not list'.format(lst))
        self._length = len(lst)
        if self._length <= 100:
            self._elements = [None for i in range(100)]
        else:
            self._elements = [None for i in range(self.length + 100)]
        for i in range(len(lst)):
            self._elements[i] = lst[i]

    def __iter__(self):
        return Next(self)

    def __eq__(self, other):
        if (other is None) or (size(other) != size(self)) or (type(other) != type(self)):
            return False
        for i in range(size(other)):
            if self._elements[i] != other._elements[i]:
                return False
        return True


class Next:
    def __init__(self, dynamic_arr: DynamicArray):
        self._elements = dynamic_arr._elements
        self._length = dynamic_arr._length
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._length:
            x = self._elements[self._index]
            self._index += 1
            return x
        else:
            raise StopIteration


def size(arr):
    """ Get the size of dynamic array """
    if arr is None:
        return 0
    elif not isinstance(arr, DynamicArray):
        raise TypeError('\'{}\' is not DynamicArray'.format(arr))
    return arr._length


def from_list(lst: list):
    """ Construct a dynamic array from a list """
    arr = DynamicArray([])
    while len(lst) > len(arr._elements):
        resize(arr, 2)
    for i in range(len(lst)):
        arr._elements[i] = lst[i]
    arr._length = len(lst)
    return arr


def to_list(arr):
    """ Convert dynamic array to list """
    lst = []
    if arr is not None:
        if not isinstance(arr, DynamicArray):
            raise TypeError('\'{}\' is not DynamicArray'.format(arr))
        for item in arr:
            lst.append(item)
    return lst


def find(arr, value):
    """ Find in the dynamic array whether there is an element with a value equal to 'value' """
    if not isinstance(arr, DynamicArray):
        raise TypeError('\'{}\' is not DynamicArray'.format(arr))
    if arr is not None:
        for item in arr:
            if item is value:
                return True
    return False


def arr_filter(arr, is_even: bool):
    """ Filter data structure by specific predicate """
    if not isinstance(arr, DynamicArray):
        raise TypeError('\'{}\' is not DynamicArray'.format(arr))
    lst = []
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
    if not callable(func):
        raise TypeError('\'{}\' object is not callable'.format(func))
    if not isinstance(arr, DynamicArray):
        raise TypeError('\'{}\' is not DynamicArray'.format(arr))
    lst = []
    for item in arr:
        if item is not None:
            lst.append(func(item))
    return DynamicArray(lst)


def arr_reduce(func, arr, initializer):
    """ Apply function of two arguments cumulatively to the items of array """
    if not callable(func):
        raise TypeError('\'{}\' object is not callable'.format(func))
    if not isinstance(arr, DynamicArray):
        raise TypeError('\'{}\' is not DynamicArray'.format(arr))
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
    if not isinstance(arr, DynamicArray):
        raise TypeError('\'{}\' is not DynamicArray'.format(arr))
    temp = [None] * len(arr._elements) * growth_factor
    for i in range(size(arr)):
        temp[i] = arr._elements[i]
    arr._elements = temp


def append(arr, item):
    """ Append a new item to array """
    if not isinstance(arr, DynamicArray):
        raise TypeError('\'{}\' is not DynamicArray'.format(arr))
    tmp = [e for e in arr]
    tmp.append(item)
    return DynamicArray(tmp)


def remove(arr, value):
    """ Remove an item whose value equal to 'value' from array """
    if find(arr, value) is False:
        raise ValueError('Can not find \'{}\' in {}'.format(value, arr))
    lst = to_list(arr)
    tmp = []
    for item in lst:
        if item != value:
            tmp.append(item)
    return DynamicArray(tmp)


def reverse(arr):
    """ Reverse the dynamic array """
    if arr is None:
        return None
    else:
        lst = []
        for i in range(size(arr) - 1, -1, -1):
            lst.append(arr._elements[i])
        return lst


def mempty():
    """ Empty the dynamic array"""
    return None


def mconcat(a, b):
    """ Concatenate two arrays a and b """
    l1 = to_list(a)
    l2 = to_list(b)
    return DynamicArray(l1 + l2)
