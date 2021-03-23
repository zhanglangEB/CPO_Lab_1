import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable import *


class TestImmutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size(None), 0)
        self.assertEqual(size(DynamicArray([1])), 1)
        self.assertEqual(size(DynamicArray([1, 2])), 2)

    def test_to_list(self):
        lst = [1, 2]
        arr = DynamicArray(lst)
        lst_arr = to_list(arr)
        self.assertEqual(to_list(None), [])
        self.assertEqual(lst, lst_arr)

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = from_list(e)
            self.assertEqual(to_list(lst), e)

    def test_find(self):
        arr = DynamicArray([1, 2])
        self.assertEqual(find(arr, 1), True)
        self.assertEqual(find(None, 1), False)

    def test_append(self):
        arr = DynamicArray([1, 2])
        self.assertEqual(to_list(append(arr, 3)), [1, 2, 3])

    def test_remove(self):
        a = DynamicArray([1, 2, 3])
        b = remove(a, 1)
        self.assertEqual(to_list(b), [2, 3])

    def test_filter(self):
        a = DynamicArray([1, 2, 3])
        b = arr_filter(a, False)
        self.assertEqual(to_list(b), [1, 3])

    def test_map(self):
        a = DynamicArray([1, 2, 3])
        b = arr_map(lambda x: x + 1, a)
        self.assertEqual(to_list(b), [2, 3, 4])

    def test_reduce(self):
        arr = DynamicArray()
        self.assertEqual(arr_reduce((lambda x, y: x + y), arr, 0), 0)
        arr = from_list([1, 2])
        self.assertEqual(arr_reduce((lambda x, y: x + y), arr, 0), 3)

    def test_mconcat(self):
        a = DynamicArray([1, 2])
        b = DynamicArray([3, 4])
        c = mconcat(a, b)
        self.assertEqual(to_list(c), [1, 2, 3, 4])

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
        lst1 = from_list(a)
        lst2 = from_list(b)
        lst3 = from_list(c)
        self.assertEqual(mconcat(mconcat(lst1, lst2), lst3), mconcat(lst1, mconcat(lst2, lst3)))

    def test_iter(self):
        x = [1, 2, 3, 4]
        lst = from_list(x)
        tmp = []
        try:
            get_next = iterator(lst)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(lst), tmp)
        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())

    def test_eq(self):
        other = from_list([1, 2, 3])
        arr = DynamicArray([1, 2, 3, 4])
        self.assertEqual(arr == other, False)
        other = append(other, 4)
        self.assertEqual(arr == other, True)


if __name__ == '__main__':
    unittest.main()
