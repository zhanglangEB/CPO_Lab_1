from mutable import *
import hypothesis.strategies as st
from hypothesis import given
import unittest


class TestMutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(DynamicArray_mut().size(), 0)
        self.assertEqual(DynamicArray_mut(['a','b','c']).size(), 3)

    def test_add(self):
        lst=DynamicArray_mut()
        lst.add(1)
        self.assertEqual(lst.to_list(),[1])

    def test_resize(self):
        lst = DynamicArray_mut()
        growing_factor = 2
        lst.resize(growing_factor)
        self.assertEqual(lst._capacity, 20)

    def test_to_list(self):
        self.assertEqual(DynamicArray_mut().to_list(), [])
        self.assertEqual(DynamicArray_mut(['a','b','c']).to_list(), ['a','b','c'])

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for val in test_data:
            lst = DynamicArray_mut()
            lst.from_list(val)
            self.assertEqual(lst.to_list(), val)

    def test_map(self):
        lst = DynamicArray_mut()
        lst.map(str)
        self.assertEqual(lst.to_list(), [])
        lst = DynamicArray_mut([1, 2, 3])
        lst.map(str)
        self.assertEqual(lst.to_list(), ["1", "2", "3"])

    def test_reduce(self):
        lst = DynamicArray_mut()
        self.assertEqual(lst.reduce(lambda st, val: st + val, 0), 0)
        lst = DynamicArray_mut([1, 2, 3])
        self.assertEqual(lst.reduce(lambda st, val: st + val, 0), 6)
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for val in test_data:
            lst = DynamicArray_mut()
            lst.from_list(val)
            self.assertEqual(lst.reduce(lambda state, _: state + 1, 0), lst.size())

    def test_find(self):
        lst = DynamicArray_mut()
        self.assertEqual(lst.find(1), False)
        lst = DynamicArray_mut([1, 2, 3])
        self.assertEqual(lst.find(1), True)

    def test_filter(self):
        lst = DynamicArray_mut()
        self.assertEqual(lst.filter(1), [])
        lst = DynamicArray_mut([1, 2, 3])
        self.assertEqual(lst.filter(1), [2, 3])

    def test_mconcat(self):
        lst = DynamicArray_mut()
        lst1 = DynamicArray_mut([1, 2, 3])
        lst2 = DynamicArray_mut([1, 2, 3])
        lst.mconcat(lst1, lst2)
        self.assertEqual(lst.to_list(), [1, 2, 3, 1, 2, 3])

    def test_remove(self):
        lst = DynamicArray_mut([1, 2, 3])
        lst.remove(1)
        self.assertEqual(lst.to_list(), [2, 3])

    def test_reverse(self):
        lst = DynamicArray_mut([1, 2, 3])
        self.assertEqual(lst.reverse(),[3,2,1])

    def test_mempty(self):
        self.assertEqual(DynamicArray_mut().mempty(),None)

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        lst = DynamicArray_mut()
        lst.from_list(a)
        b = lst.to_list()
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst2 = DynamicArray_mut()
        lst2.from_list(a)
        self.assertEqual(lst2.size(), len(a))

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, li):
        lst = DynamicArray_mut()
        lst.from_list(li)
        self.assertEqual(lst.mconcat(lst.mempty(), lst.to_list()), li)
        self.assertEqual(lst.mconcat(lst.to_list(), lst.mempty()), li)

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        lst = DynamicArray_mut()
        lst1 = DynamicArray_mut(a)
        lst2 = DynamicArray_mut(b)
        lst3 = DynamicArray_mut(c)
        self.assertEqual(lst.mconcat(lst.mconcat(lst1.to_list(), lst2.to_list()), lst3.to_list()),
                         lst.mconcat(lst1.to_list(), lst.mconcat(lst2.to_list(), lst3.to_list())))

    def test_iter(self):
        x = [1, 2, 3]
        lst = DynamicArray_mut()
        lst.from_list(x)
        tmp = []
        for val in lst:
            tmp.append(val)
        self.assertEqual(x, tmp)
        self.assertEqual(lst.to_list(), tmp)
        i = iter(DynamicArray_mut())
        self.assertRaises(StopIteration, lambda: next(i))


if __name__ == '__main__':
    unittest.main()
