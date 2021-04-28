import sys
import os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

import unittest
from immutable import *
from hypothesis import given
import hypothesis.strategies as st


class TestImmutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size(None), 0)
        self.assertEqual(size(DynamicArray([None])), 1)
        self.assertEqual(size(DynamicArray([1, 2])), 2)
        self.assertRaises(TypeError, lambda: size('str'))

    def test_to_list(self):
        lst = [1, 2]
        arr = DynamicArray(lst)
        lst_arr = to_list(arr)
        self.assertEqual(to_list(None), [])
        self.assertEqual(lst, lst_arr)
        self.assertRaises(TypeError, lambda: to_list('str'))

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = from_list(e)
            self.assertEqual(to_list(lst), e)
        with self.assertRaises(TypeError):
            from_list(2)

    def test_find(self):
        arr = DynamicArray([1, 2])
        self.assertEqual(find(arr, 1), True)
        self.assertRaises(TypeError, lambda: find(None, 1))

    def test_resize(self):
        a = DynamicArray()
        resize(a, 2)
        self.assertEqual(len(a._elements), 200)
        with self.assertRaises(TypeError):
            resize(a, "hello")

    def test_append(self):
        arr = DynamicArray([1, 2])
        self.assertEqual(to_list(append(arr, 3)), [1, 2, 3])

    def test_remove(self):
        a = DynamicArray([1, 2, 3])
        b = remove(a, 1)
        self.assertEqual(to_list(b), [2, 3])
        self.assertRaises(ValueError, lambda: remove(a, 5))
        self.assertRaises(TypeError, lambda: remove(None, 5))

    def test_filter(self):
        a = DynamicArray([1, 2, 3])
        b = arr_filter(a, False)
        self.assertEqual(to_list(b), [1, 3])
        self.assertRaises(TypeError, lambda: arr_filter(None, True))

    def test_map(self):
        a = DynamicArray([1, 2, 3])
        b = arr_map(lambda x: x + 1, a)
        self.assertEqual(to_list(b), [2, 3, 4])
        c = DynamicArray(['a', 1, 'b'])
        self.assertRaises(TypeError, lambda: arr_map(lambda x: x + 1, c))
        self.assertRaises(TypeError, lambda: arr_map(None, None))

    def test_reduce(self):
        arr = DynamicArray()
        self.assertEqual(arr_reduce((lambda x, y: x + y), arr, 0), 0)
        arr = from_list([1, 2])
        self.assertEqual(arr_reduce((lambda x, y: x + y), arr, 0), 3)
        self.assertRaises(TypeError, lambda: arr_reduce((lambda x, y: x + y), arr, 'str'))

    def test_mempty(self):
        self.assertEqual(mempty(), None)

    def test_mconcat(self):
        a = DynamicArray([1, 2])
        b = DynamicArray([3, 4])
        c = mconcat(a, b)
        d = mconcat(None, b)
        self.assertEqual(to_list(c), [1, 2, 3, 4])
        self.assertEqual(to_list(d), [3, 4])

    def test_reverse(self):
        self.assertEqual(reverse(None), None)
        arr1 = DynamicArray(['a'])
        arr2 = DynamicArray(['a', 'b'])
        arr3 = DynamicArray(['b', 'a'])
        self.assertEqual(reverse(arr1), to_list(arr1))
        self.assertEqual(reverse(arr2), to_list(arr3))

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        self.assertEqual(to_list(from_list(a)), a)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = from_list(lst)
        self.assertEqual(mconcat(mempty(), a), a)
        self.assertEqual(mconcat(a, mempty()), a)

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        arr1 = from_list(a)
        arr2 = from_list(b)
        arr3 = from_list(c)
        self.assertEqual(mconcat(mconcat(arr1, arr2), arr3), mconcat(arr1, mconcat(arr2, arr3)))

    @given(a=st.lists(st.integers()))
    def test_immutability(self, a):
        arr1 = from_list(a)
        arr2 = arr1
        arr2 = append(arr2, 1)
        self.assertNotEqual(arr1, arr2)

    def test_iter(self):
        x = [1, 2, 3, 4]
        arr = from_list(x)
        tmp = [item for item in arr]
        it1 = iter(arr)
        it2 = iter(arr)
        self.assertEqual(x, tmp)
        self.assertEqual(next(it1), next(it2))
        it3 = iter(DynamicArray([]))
        self.assertRaises(StopIteration, lambda: next(it3))

    def test_eq(self):
        other = from_list([1, 2, 3])
        arr = DynamicArray([1, 2, 3, 4])
        self.assertEqual(arr == other, False)
        other = append(other, 4)
        self.assertEqual(arr == other, True)


if __name__ == '__main__':
    unittest.main()
