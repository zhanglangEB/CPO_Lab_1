class DynamicArray_mut(object):

    def __init__(self,lst=[]):
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
        self.a = 0
        return self

    def __next__(self):
        if self._elements[self.a] is not None:
            x = self._elements[self.a]
            self.a += 1
            return x
        else:
            raise StopIteration

    def size(self):
        return self._length

    def from_list(self, lst):
        while(len(lst)>self._capacity):
            self.resize(2)
        for i in range(len(lst)):
            self._elements[i] = lst[i]
        self._length = len(lst)
        return self

    def to_list(self):
        lst = []
        for value in self._elements:
            if value is not None:
                lst.append(value)
        return lst

    def resize(self,growth_factor):
        newelements = [None] * self._capacity * growth_factor
        for i in range(self._length):
            newelements[i] = self._elements[i]
        self._elements = newelements
        self._capacity *= growth_factor

    def add(self, value):
        if self._length == self._capacity:
            self.resize(2)
        self._elements[self._length] = value
        self._length += 1

    def find(self,value):
        lst=self.to_list()
        for val in lst:
            if val is value:
                return True
        return False

    def filter(self, value):
        lst_filter = []
        for i in self._elements[:self._length]:
            if i is not value:
                lst_filter.append(i)
        return lst_filter

    def map(self,f):
        for i in range(self._length):
            if self._elements[i] is not None:
                self._elements[i] = f(self._elements[i])

    def reduce(self, f, initial_state):
        state = initial_state
        cur = 0
        while self._elements[cur] is not None:
            state = f(state, self._elements[cur])
            cur += 1
        return state


    def remove(self, value):
        for i in range(self._length):
            if self._elements[i] == value:
                for j in range(i, self._length - 1):
                    self._elements[j] = self._elements[j + 1]
                self._elements[self._length - 1] = None
                self._length -= 1
                return
        raise ValueError('value not found')

    def mempty(self):
        return None

    def mconcat(self,lst1,lst2):
        lst=DynamicArray_mut([])
        if lst1 is  None:
            for val in lst2._elements:
                lst.add(val)
        elif lst2 is  None:
            for val in lst1._elements:
                lst.add(val)
        else:
            for val in lst1._elements:
                lst.add(val)
            for val in lst2._elements:
                lst.add(val)
        return lst

    def reverse(self):
        arr=[]
        for i in range(self._length -1 ,-1 ,-1):
            arr.append(self._elements[i])
        return arr;

