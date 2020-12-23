# -*- coding: utf-8 -*-
"""
@author: narendra
"""

# Program to perform sorting using Bubble Sort method

# bubble sort function to sort the input array
def bubble_sort(arr1): 
    n = len(arr1) 
    
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater than the next element 
            if arr1[j] > arr1[j+1]: 
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j] 


# Main driving code to test above 

# an array which is unsorted
arr1 = [54, 44, 15, 22, 16, 19, 80] 

# function call
bubble_sort(arr1) 

print ("Sorted array is:") 
for i in range(len(arr1)): 
    print ("%d" %arr1[i]),