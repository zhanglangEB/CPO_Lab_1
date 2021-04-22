import unittest
from immutable import *
from hypothesis import given
import hypothesis.strategies as st


class TestImmutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size(None), 0)
        self.assertEqual(size(DynamicArray([None])), 1)
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
        with self.assertRaises(TypeError):
            from_list(2)

    def test_find(self):
        arr = DynamicArray([1, 2])
        self.assertEqual(find(arr, 1), True)
        self.assertEqual(find(None, 1), False)

    def test_resize(self):
        a = DynamicArray()
        resize(a, 2)
        self.assertEqual(len(a.elements), 200)
        with self.assertRaises(TypeError):
            resize(a, "hello")

    def test_append(self):
        arr = DynamicArray([1, 2])
        self.assertEqual(to_list(append(arr, 3)), [1, 2, 3])

    def test_remove(self):
        a = DynamicArray([1, 2, 3])
        b = remove(a, 1)
        self.assertEqual(to_list(b), [2, 3])
        with self.assertRaises(ValueError):
            remove(a, 5)

    def test_filter(self):
        a = DynamicArray([1, 2, 3])
        b = arr_filter(a, False)
        self.assertEqual(to_list(b), [1, 3])

    def test_map(self):
        a = DynamicArray([1, 2, 3])
        b = arr_map(lambda x: x + 1, a)
        self.assertEqual(to_list(b), [2, 3, 4])
        c = DynamicArray(['a', 1, 'b'])
        with self.assertRaises(TypeError):
            arr_map(lambda x: x+1, c)

    def test_reduce(self):
        arr = DynamicArray()
        self.assertEqual(arr_reduce((lambda x, y: x + y), arr, 0), 0)
        arr = from_list([1, 2])
        self.assertEqual(arr_reduce((lambda x, y: x + y), arr, 0), 3)
        with self.assertRaises(TypeError):
            arr_reduce((lambda x, y: x + y), arr, "this is a string")

    def test_mempty(self):
        self.assertEqual(mempty(), None)

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
        arr1 = from_list(a)
        arr2 = from_list(b)
        arr3 = from_list(c)
        self.assertEqual(mconcat(mconcat(arr1, arr2), arr3), mconcat(arr1, mconcat(arr2, arr3)))

    def test_iter(self):
        x = [1, 2, 3, 4]
        arr = from_list(x)
        tmp = [item for item in arr]
        it1 = iter(arr)
        it2 = iter(arr)
        self.assertEqual(x, tmp)
        self.assertEqual(next(it1), next(it2))
        it3 = iter(DynamicArray([]))
        with self.assertRaises(StopIteration):
            next(it3)

    def test_eq(self):
        other = from_list([1, 2, 3])
        arr = DynamicArray([1, 2, 3, 4])
        self.assertEqual(arr == other, False)
        other = append(other, 4)
        self.assertEqual(arr == other, True)


if __name__ == '__main__':
    unittest.main()
