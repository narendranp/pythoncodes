# -*- coding: utf-8 -*-
"""
@author: narendra
"""

# Program to perform searching using Binary search method

# Iterative Binary search Function 
# The function returns the index of x in a given array arr if present, 
# else returns -1 
def binary_search(arr1, x): 
    low = 0
    high = len(arr1) - 1
    mid = 0
    
    while low <= high: 
        
        mid = (high + low) // 2
        
        # Check if x is present at mid 
        if arr1[mid] < x: 
            low = mid + 1
        
        # If x is greater, ignore left half 
        elif arr1[mid] > x: 
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            return mid 
  
    # If we reach here, then the element was not present 
    return -1


# Main driving code to test above 

# Test array 
arr1 = [ 2, 3, 4, 10, 40 ] 
x = 4 # element to be searched in array
  
# Function call 
result = binary_search(arr1, x) 

if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 