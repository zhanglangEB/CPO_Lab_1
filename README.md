# Dynamic array
   **group name**: oh my nunu     
   **list of group members**: Xin, Wang、Qianwen, Yu   
   **laboratory work number**: 1  
   **variant description**: Dynamic array  
# Synopsis
   **Use python to develop a library to implement dynamic arrays, which must meet the following conditions:** 

   1. Make sure the implementation correctly works with None value. 
   2. Implement functions/methods for getting/setting value by index. 
   3. When the memory chunk is not enough, new space must be allocated.  

   **The dynamic array structure should be implemented in two versions:**  

   1. mutable version.   
   2. immutable version.

   **The following functions should be implemented in both mutable version and immutable version:**  

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
   **Qianyu, Wen(github: yqw123)**: Complete the mutable version dynamic array and the tests of the mutable version.Finish part of the report.   
   **Xin, Wang(github: zhanglangEB)**: Complete the immutable version dynamic array and the tests of the immutable version.Finish part of the report.  

# Explanation of taken design decisions and analysis
   The difference between dynamic arrays and ordinary arrays is that dynamic arrays can be dynamically expanded. When using ordinary arrays, we usually need to specify the number of array elements or the size of the array. But sometimes, we do not want to limit the size of the array, at this time, the advantages of dynamic arrays are reflected.  

  We implement dynamic arrays by using static arrays in python. The way we achieve dynamic expansion is to allocate new memory for the array to store elements when we find that the memory of the array is insufficient.   

# Work demonstration
   **mutable version:**   
   1. size  

      ```
      self.assertEqual(DynamicArray_mut(['a','b','c']).size(), 3)
      ```

   2. add  

      ```
      lst=DynamicArray_mut()  
      lst.add(1)  
      self.assertEqual(lst.to_list(),[1]) 
      ```

   3. from_list  

      ```
      lst = DynamicArray_mut()  
      lst.from_list(['a']) 
      self.assertEqual(lst.to_list(), e) 
      ```

   4. to_list 

      ```
      self.assertEqual(DynamicArray_mut(['a','b','c']).to_list(), ['a','b','c'])
      ```

   5. find  
	
      ```
      self.assertEqual(DynamicArray_mut([1, 2, 3]).find(1), True)
      ```
	
   6. filter  
   
      ```
      self.assertEqual(DynamicArray_mut().filter(1), [])
      ```

   7. map  

      ```
      self.assertEqual(DynamicArray_mut([1,2,3]).map(str).to_list(), ["1", "2", "3"])
      ```

   8. reduce  

      ```
      self.assertEqual(DynamicArray_mut([1,2,3]).reduce(lambda st, e: st + e, 0), 6)
      ```

   9. remove  

      ```
      self.assertEqual(DynamicArray_mut([1, 2, 3]).remove(1).to_list(), [2, 3])
      ```

   10. reverse  

       ```
       self.assertEqual(DynamicArray_mut([1, 2, 3]).reverse(),[3,2,1])
       ```

   11. mconcat  

       ```
       lst = DynamicArray_mut()
       lst1 = [1, 2, 3]
       lst2 = [1, 2, 3] 
       lst.mconcat(lst1, lst2) 
       self.assertEqual(lst.to_list(), [1, 2, 3, 1, 2, 3])  
       ```

   12. iter

       ```
       x = [1, 2, 3]
       lst = DynamicArray_mut()
       lst.from_list(x)
       tmp = []
       for val in lst:
       	tmp.append(val)    
       self.assertEqual(x, tmp) 
       ```

   13. mempty 

       ```
       self.assertEqual(DynamicArray_mut().mempty(),None)
       ```

   **immutable version:**   
   1. size   

         ```
         self.assertEqual(size(DynamicArray([1])), 1)
         ```

   2. from_list   

         ```
         test_data = [[],['a'],['a', 'b']] 
         for e in test_data: 
         lst = from_list(e) 
         self.assertEqual(to_list(lst), e)
         ```

   3. to_list   

       ```
       lst = [1, 2]
       arr = DynamicArray(lst)
       lst_arr = to_list(arr) 
       self.assertEqual(lst, lst_arr)
       ```

   4. find   

         ```
         arr = DynamicArray([1, 2])  
         self.assertEqual(find(arr, 1), True)
         ```

   5. arr_filter  

         ```
         is_even = False
         a = DynamicArray([1, 2, 3])  
         b = arr_filter(a, is_even)  
         self.assertEqual(to_list(b), [1, 3])   
         ```

   6. arr_map  

         ```
         a = DynamicArray([1, 2, 3])  
         b = arr_map(lambda x: x + 1, a)  
         self.assertEqual(to_list(b), [2, 3, 4])   
         ```

   7. append   

         ```
         arr = DynamicArray([1, 2])  
         self.assertEqual(to_list(append(arr, 3)), [1, 2, 3])  
         ```

   8. remove  

         ```
         a = DynamicArray([1, 2, 3])  
         b = remove(a, 1)  
         self.assertEqual(to_list(b), [2, 3]) 
         ```

   9. reverse   

         ```
         arr1 = DynamicArray(['a'])  
         arr2 = DynamicArray(['a', 'b'])  
         arr3 = DynamicArray(['b', 'a'])  
         self.assertEqual(reverse(arr1), to_list(arr1))  
         self.assertEqual(reverse(arr2), to_list(arr3))
         ```

   10. mempty   

        ```
        self.assertEqual(mempty(), None)  
        ```

   11. mconcat   

        ```
        a = DynamicArray([1, 2])  
        b = DynamicArray([3, 4])  
        c = mconcat(a, b)  
        self.assertEqual(to_list(c), [1, 2, 3, 4])   
        ```

   12. iterator

        ```
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
        ```

# Conclusion
  The dynamic array can use memory flexibly and effectively, it does not need to specify the size of the array before use, which is more convenient to use. 

  The basic types of python are divided into mutable and immutable. Mutable can be modified after creation, and immutable cannot be modified after creation. Therefore, the dynamic array we have implemented is also divided into mutable and immutable versions according to the above characteristics.In both versions, we use the basic static list type in python to implement dynamic array. When using a dynamic array, we first allocate a fixed memory to the dynamic array. When adding new elements exceeds the capacity of the dynamic array, we then apply for more memory to store the elements. In this way, we have realized the dynamic expansion of the array.