# Dynamic array
   **group name**: oh my nunu <br/>    
   **list of group members**: Xin, Wang、Qianwen, Yu <br/>    
   **laboratory work number**: 1 <br/>  
   **variant description**: Dynamic array <br/>  
# Synopsis
   **Use python to develop a library to implement dynamic arrays, which must meet the following conditions:**<br/> 
    1. Make sure the implementation correctly works with None value.<br/> 
    2. Implement functions/methods for getting/setting value by index.<br/> 
    3. When the memory chunk is not enough, new space must be allocated.<br/> <br/> 
  
   **The dynamic array structure should be implemented in two versions:**<br/> 
    1. mutable version.<br/> 
    2. immutable version.<br/> <br/> 
  
   **The following functions should be implemented in both mutable version and immutable version:**<br/> 
    1. Add a new element.<br/> 
    2. Remove an element by value.<br/> 
    3. Size, member, reverse(if applicable), intersection.<br/> 
    4. Find element by specific predicate.<br/> 
    5. Filter data structure by specific predicate.<br/> 
    6. Map structure by specific functiong.<br/> 
    7. Reduce - process structure elements to build a return value by specific functions.<br/> 
    8. Data structure should be an iterator.<br/> 
    9. Data structure should be monoid and implement mempty and mconcat.<br/> 
  
  After finishing programming, you need to verify your library by unit tests and property-based tests.<br/> <br/> 
  
# Contribution summary for each group member
   **Qianyu, Wen(github: yqw123)**: Complete the mutable version dynamic array and the tests of the mutable version.Finish part of the report.<br/> 
   **Xin, Wang(github: zhanglangEB)**: Complete the immutable version dynamic array and the tests of the immutable version.Finish part of the report.<br/> <br/> 

# Explanation of taken design decisions and analysis
   The difference between dynamic arrays and ordinary arrays is that dynamic arrays can be dynamically expanded. When using ordinary arrays, we usually need to specify the number of array elements or the size of the array. But sometimes, we do not want to limit the size of the array, at this time, the advantages of dynamic arrays are reflected.<br/> 
   We implement dynamic arrays by using static arrays in python. The way we achieve dynamic expansion is to allocate new memory for the array to store elements when we find that the memory of the array is insufficient.<br/> <br/> 

# Work demonstration
   **mutable version:**<br/> 
   **immutable version:**<br/> 
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
    12. iterator(arr)<br/> <br/> 
# Conclusion
   The dynamic array can use memory flexibly and effectively, it does not need to specify the size of the array before use, which is more convenient to use.<br/> 
   The basic types of python are divided into mutable and immutable. Mutable can be modified after creation, and immutable cannot be modified after creation. Therefore, the dynamic array we have implemented is also divided into mutable and immutable versions according to the above characteristics.In both versions, we use the basic static list type in python to implement dynamic array. When using a dynamic array, we first allocate a fixed memory to the dynamic array. When adding new elements exceeds the capacity of the dynamic array, we then apply for more memory to store the elements. In this way, we have realized the dynamic expansion of the array.
