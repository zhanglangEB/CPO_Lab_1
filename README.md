# Dynamic array
   &emsp;&emsp;**group name**: oh my nunu <br/>    
   &emsp;&emsp;**list of group members**: Xin, Wang、Qianwen, Yu <br/>    
   &emsp;&emsp;**laboratory work number**: 1 <br/>  
   &emsp;&emsp;**variant description**: Dynamic array <br/>  
# Synopsis
   &emsp;&emsp;**Use python to develop a library to implement dynamic arrays, which must meet the following conditions:**<br/> 
    &emsp;&emsp;&emsp;&emsp;1. Make sure the implementation correctly works with None value.<br/> 
    &emsp;&emsp;&emsp;&emsp;2. Implement functions/methods for getting/setting value by index.<br/> 
    &emsp;&emsp;&emsp;&emsp;3. When the memory chunk is not enough, new space must be allocated.<br/> <br/> 
  
   &emsp;&emsp;**The dynamic array structure should be implemented in two versions:**<br/> 
    &emsp;&emsp;&emsp;&emsp;1. mutable version.<br/> 
    &emsp;&emsp;&emsp;&emsp;2. immutable version.<br/> <br/> 
  
   &emsp;&emsp;**The following functions should be implemented in both mutable version and immutable version:**<br/> 
    &emsp;&emsp;&emsp;&emsp;1. Add a new element.<br/> 
    &emsp;&emsp;&emsp;&emsp;2. Remove an element by value.<br/> 
    &emsp;&emsp;&emsp;&emsp;3. Size, member, reverse(if applicable), intersection.<br/> 
    &emsp;&emsp;&emsp;&emsp;4. Find element by specific predicate.<br/> 
    &emsp;&emsp;&emsp;&emsp;5. Filter data structure by specific predicate.<br/> 
    &emsp;&emsp;&emsp;&emsp;6. Map structure by specific functiong.<br/> 
    &emsp;&emsp;&emsp;&emsp;7. Reduce - process structure elements to build a return value by specific functions.<br/> 
    &emsp;&emsp;&emsp;&emsp;8. Data structure should be an iterator.<br/> 
    &emsp;&emsp;&emsp;&emsp;9. Data structure should be monoid and implement mempty and mconcat.<br/> 
  
  &emsp;&emsp;After finishing programming, you need to verify your library by unit tests and property-based tests.<br/> <br/> 
  
# Contribution summary for each group member
   &emsp;&emsp;**Qianyu, Wen(github: yqw123)**: Complete the mutable version dynamic array and the tests of the mutable version.Finish part of the report.<br/> 
   &emsp;&emsp;**Xin, Wang(github: zhanglangEB)**: Complete the immutable version dynamic array and the tests of the immutable version.Finish part of the report.<br/> <br/> 

# Explanation of taken design decisions and analysis
   &emsp;&emsp;The difference between dynamic arrays and ordinary arrays is that dynamic arrays can be dynamically expanded. When using ordinary arrays, we usually need to specify the number of array elements or the size of the array. But sometimes, we do not want to limit the size of the array, at this time, the advantages of dynamic arrays are reflected.<br/> 
   &emsp;&emsp;We implement dynamic arrays by using static arrays in python. The way we achieve dynamic expansion is to allocate new memory for the array to store elements when we find that the memory of the array is insufficient.<br/> <br/> 

# Work demonstration
   &emsp;&emsp;**mutable version:**<br/> 
   &emsp;&emsp;&emsp;&emsp;1. size  
   &emsp;&emsp;&emsp;&emsp;&emsp;self.assertEqual(DynamicArray_mut(['a','b','c']).size(), 3)<br/> 
   &emsp;&emsp;&emsp;&emsp;2.add<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;lst=DynamicArray_mut()<br/> 
   &emsp;&emsp;&emsp;&emsp;&emsp;lst.add(1)<br/> 
   &emsp;&emsp;&emsp;&emsp;&emsp;self.assertEqual(lst.to_list(),[1])<br/> 
   &emsp;&emsp;&emsp;&emsp;3. from_list<br/> 
	&emsp;&emsp;&emsp;&emsp;&emsp;lst = DynamicArray_mut()<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;lst.from_list(['a'])<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;self.assertEqual(lst.to_list(), e)<br/>
   &emsp;&emsp;&emsp;&emsp;4. to_list<br/> 	
   &emsp;&emsp;&emsp;&emsp;&emsp;self.assertEqual(DynamicArray_mut(['a','b','c']).to_list(), ['a','b','c'])<br/>
   &emsp;&emsp;&emsp;&emsp;5. find<br/> 
	&emsp;&emsp;&emsp;&emsp;&emsp;self.assertEqual(DynamicArray_mut([1, 2, 3]).find(1), True)<br/>
   &emsp;&emsp;&emsp;&emsp;6. filter<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;self.assertEqual(DynamicArray_mut().filter(1), [])<br/>
   &emsp;&emsp;&emsp;&emsp;7. map<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;self.assertEqual(DynamicArray_mut([1,2,3]).map(str).to_list(), ["1", "2", "3"])<br/>
   &emsp;&emsp;&emsp;&emsp;8. reduce<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;self.assertEqual(DynamicArray_mut([1,2,3]).reduce(lambda st, e: st + e, 0), 6)<br/>
   &emsp;&emsp;&emsp;&emsp;9. remove<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;self.assertEqual(DynamicArray_mut([1, 2, 3]).remove(1).to_list(), [2, 3])<br/>
   &emsp;&emsp;&emsp;&emsp;10.reverse<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;self.assertEqual(DynamicArray_mut([1, 2, 3]).reverse(),[3,2,1])<br/>
   &emsp;&emsp;&emsp;&emsp;11.mconcat<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;lst = DynamicArray_mut()<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;lst1 = [1, 2, 3]<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;lst2 = [1, 2, 3]<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;lst.mconcat(lst1, lst2)<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;self.assertEqual(lst.to_list(), [1, 2, 3, 1, 2, 3])<br/>
   &emsp;&emsp;&emsp;&emsp;12.iter<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;x = [1, 2, 3]<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;lst = DynamicArray_mut()<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;lst.from_list(x)<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;tmp = []<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;for val in lst:<br/>
   &emsp;&emsp;&emsp;&emsp;&emsp;tmp.append(val) <br/> 
   &emsp;&emsp;&emsp;&emsp;&emsp;self.assertEqual(x, tmp)<br/>
   &emsp;&emsp;**immutable version:**<br/> 
   &emsp;&emsp;&emsp;&emsp;1. size(arr)<br/> 
   &emsp;&emsp;&emsp;&emsp;arr represents a dynamic array, it can be constructed by a list using DynamicArray(lst).The following arr are the same.<br/> 
   &emsp;&emsp;&emsp;&emsp;lst represents a list in python(eg. lst = [1, 2, 3]).The following lst are the same.<br/> 
   &emsp;&emsp;&emsp;&emsp;2. from_list(lst)<br/> 
   &emsp;&emsp;&emsp;&emsp;3. to_list(arr)<br/> 
   &emsp;&emsp;&emsp;&emsp;4. find(arr, value)<br/> 
   &emsp;&emsp;&emsp;&emsp;5. arr_filter(arr, is_even)<br/> 
   &emsp;&emsp;&emsp;&emsp;if is_even is true, arr_filter returns a dynamic array only containing even elements in arr.<br/> 
   &emsp;&emsp;&emsp;&emsp;else it returns odd dynamic array.<br/> 
   &emsp;&emsp;&emsp;&emsp;6. arr_map(func, arr)<br/> 
   &emsp;&emsp;&emsp;&emsp;func represents a function applied to the array.<br/> 
   &emsp;&emsp;&emsp;&emsp;7. append(arr, item)<br/> 
   &emsp;&emsp;&emsp;&emsp;8. remove(arr, value)<br/> 
   &emsp;&emsp;&emsp;&emsp;9. reverse(arr)<br/> 
   &emsp;&emsp;&emsp;&emsp;10. mempty()<br/> 
   &emsp;&emsp;&emsp;&emsp;11. mconcat(a, b)<br/> 
   &emsp;&emsp;&emsp;&emsp;a and b are two dynamic arrays.<br/> 
   &emsp;&emsp;&emsp;&emsp;12. iterator(arr)<br/> <br/> 
# Conclusion
   &emsp;&emsp;The dynamic array can use memory flexibly and effectively, it does not need to specify the size of the array before use, which is more convenient to use.<br/> 
   &emsp;&emsp;The basic types of python are divided into mutable and immutable. Mutable can be modified after creation, and immutable cannot be modified after creation. Therefore, the dynamic array we have implemented is also divided into mutable and immutable versions according to the above characteristics.In both versions, we use the basic static list type in python to implement dynamic array. When using a dynamic array, we first allocate a fixed memory to the dynamic array. When adding new elements exceeds the capacity of the dynamic array, we then apply for more memory to store the elements. In this way, we have realized the dynamic expansion of the array.
