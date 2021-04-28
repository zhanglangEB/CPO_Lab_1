class DynamicArray_mut(object):

    def __init__(self, lst=[]):
        self._length = 0
        self._capacity = 10
        self._elements = [None] * self._capacity
        while (len(lst) > self._capacity):
            self.resize(2)
        for i in range(len(lst)):
            self._elements[i] = lst[i]
        self._length = len(lst)

    def __len__(self):
        return self._length

    def __getitem__(self, n):
        if not 0 <= n < self._length:
            raise ValueError('invalid index')
        return self._elements[n]

    def __eq__(self, other):
        if other is None:
            return False
        for i in range(100):
            if self._elements[i] != other._elements[i]:
                return False
        return True

    def __iter__(self):
        return Next(self)

    def size(self):
        """ Get the size of dynamic array """
        return self._length

    def from_list(self, lst: list):
        """ Construct a dynamic array from a list """
        while (len(lst) > self._capacity):
            self.resize(2)
        for i in range(len(lst)):
            self._elements[i] = lst[i]
        self._length = len(lst)
        return self

    def to_list(self):
        """ Convert dynamic array to list """
        lst = []
        for value in self._elements:
            if value is not None:
                lst.append(value)
        return lst

    def resize(self, growth_factor: int):
        """ Resize the dynamic array according to growth factor"""
        newelements = [None] * self._capacity * growth_factor
        for i in range(self._length):
            newelements[i] = self._elements[i]
        self._elements = newelements
        self._capacity *= growth_factor

    def add(self, value):
        """ Add a new item to array """
        if self._length == self._capacity:
            self.resize(2)
        self._elements[self._length] = value
        self._length += 1

    def find(self, value):
        """ Find in the dynamic array whether there is an element with a value equal to 'value' """
        lst = self.to_list()
        for val in lst:
            if val is value:
                return True
        return False

    def filter(self, value):
        """ Filter data structure by specific predicate """
        lst_filter = []
        for i in self._elements[:self._length]:
            if i is not value:
                lst_filter.append(i)
        return lst_filter

    def map(self, f):
        """ Apply function to every item in array """
        if not callable(f):
            raise TypeError('\'{}\' object is not callable'.format(f))
        for i in range(self._length):
            if self._elements[i] is not None:
                self._elements[i] = f(self._elements[i])

    def reduce(self, f, initial_state):
        """ Apply function of two arguments cumulatively to the items of array """
        if not callable(f):
            raise TypeError('\'{}\' object is not callable'.format(f))
        state = initial_state
        cur = 0
        while self._elements[cur] is not None:
            state = f(state, self._elements[cur])
            cur += 1
        return state

    def remove(self, value):
        """ Remove an item whose value equal to 'value' from array """
        for i in range(self._length):
            if self._elements[i] == value:
                for j in range(i, self._length - 1):
                    self._elements[j] = self._elements[j + 1]
                self._elements[self._length - 1] = None
                self._length -= 1
                return
        raise ValueError('Can not find \'{}\' in {}'.format(value, self))

    def mempty(self):
        """ Empty the dynamic array"""
        return None

    def mconcat(self, lst):
        """ Concatenate self with lst """
        if lst is not None:
            if not isinstance(lst, DynamicArray_mut):
                raise TypeError('\'{}\' is not DynamicArray_mut'.format(lst))
            for val in lst._elements:
                self.add(val)
        return self

    def reverse(self):
        """ Reverse the dynamic array """
        arr = []
        for i in range(self._length - 1, -1, -1):
            arr.append(self._elements[i])
        return arr


class Next:
    def __init__(self, dynamic_arr: DynamicArray_mut):
        self._elements = dynamic_arr._elements
        self._length = dynamic_arr._length
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._elements[self.a] is not None:
            x = self._elements[self.a]
            self.a += 1
            return x
        else:
            raise StopIteration
