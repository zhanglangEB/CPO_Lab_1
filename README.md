# Dynamic array
  group name: oh my nunu
  list of group members: Xin, Wang、Qianwen, Yu
  laboratory work number: 1
  variant description: Dynamic array
# Synopsis
  Use python to develop a library to implement dynamic arrays, which must meet the following conditions:
    1. Make sure the implementation correctly works with None value.
    2. Implement functions/methods for getting/setting value by index.
    3. When the memory chunk is not enough, new space must be allocated.
  
  The dynamic array structure should be implemented in two versions:
    1. mutable version.
    2. immutable version.
  
  The following functions should be implemented in both mutable version and immutable version:
    1. Add a new element.
    2. Remove an element by value.
    3. Size, member, reverse(if applicable), intersection.
    4. Find element by specific predicate.
    5. Filter data structure by specific predicate.
    6. Map structure by specific functiong.
    7. Reduce - process structure elements to build a return value by specific functions.
    8. Data structure should be an iterator.
    9. Data structure should be monoid and implement mempty and mconcat.
  
  After finishing programming, you need to verify your library by unit tests and property-based tests.
  
# Contribution summary for each group member
  Qianyu, Wen(github: yqw123): Complete the mutable version dynamic array and the tests of the mutable version.Finish part of the report.
  Xin, Wang(github: zhanglangEB): Complete the immutable version dynamic array and the tests of the immutable version.Finish part of the report.

# Explanation of taken design decisions and analysis
  The difference between dynamic arrays and ordinary arrays is that dynamic arrays can be dynamically expanded. When using ordinary arrays, we usually need to specify the number of array elements or the size of the array. But sometimes, we do not want to limit the size of the array, at this time, the advantages of dynamic arrays are reflected.
  We implement dynamic arrays by using static arrays in python. The way we achieve dynamic expansion is to allocate new memory for the array to store elements when we find that the memory of the array is insufficient.

# Work demonstration
  mutable version:
  immutable version:
  1. size(arr)
    arr represents a dynamic array, it can be constructed by a list using DynamicArray(lst).The following arr are the same.
    lst represents a list in python(eg. lst = [1, 2, 3]).The following lst are the same.
  2. from_list(lst)
  3. to_list(arr)
  4. find(arr, value)
  5. arr_filter(arr, is_even)
    if is_even is true, arr_filter returns a dynamic array only containing even elements in arr.
    else it returns odd dynamic array.
  6. arr_map(func, arr)
    func represents a function applied to the array.
  7. append(arr, item)
  8. remove(arr, value)
  9. reverse(arr)
  10. mempty()
  11. mconcat(a, b)
    a and b are two dynamic arrays.
  12. iterator(arr)
# Conclusion
  The dynamic array can use memory flexibly and effectively, it does not need to specify the size of the array before use, which is more convenient to use.
  The basic types of python are divided into mutable and immutable. Mutable can be modified after creation, and immutable cannot be modified after creation. Therefore, the dynamic array we have implemented is also divided into mutable and immutable versions according to the above characteristics.In both versions, we use the basic static list type in python to implement dynamic array. When using a dynamic array, we first allocate a fixed memory to the dynamic array. When adding new elements exceeds the capacity of the dynamic array, we then apply for more memory to store the elements. In this way, we have realized the dynamic expansion of the array.
