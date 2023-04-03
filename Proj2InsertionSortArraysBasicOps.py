# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 22:36:13 2023

@author: moozi
"""
global arr, sortedarray

import time

"""
this method gathers the file name and parses the values in the file into an
array
"""
def input_filename_to_array():
    #ask user for file name
    infilename = input("Enter the name of the file you want to sort (include .txt)")
    #the next line may need to be edited depending on your directory/computer
    path = "C:/Users/moozi/Downloads/Fireshot/" + infilename
    #the next line prints the directory path 
    #print(path)
    infile = open(path , "r")
    
    #write the file into an array
    arr = []
    
    for line in infile:
        data = line.strip("\n").split()
        
        for i, item in enumerate(data):
            arr.append(data)
    print(arr)
    """            
    the next two lines can be uncommented to check that the file populated
    into the array correctly, and that the number of elements in the array
    match the number of values in the file
    """    
    #print(arr)
    #print(len(arr))
    return(arr)
    

"""
This method implements the insertion sort algorithm using the array we created
in our method below.
"""

def insertion_sort_array(arr):
    """
    vars and their purposes:
        x: value of the "key" being sorted at that time
        n: length of original array
        i: index to navigate the original array
        j: index of x
        arr[]: original array
        sortedarr[]: the sorted array. This will be appended to after every 
        sorting loop
    """
    #print(len(arr))
    sortedarray= arr
    
    n = len(arr)
    i = 2
    basicops = 0   
    
    for i in range(n):
        x = arr[i]
        j = i - 1
        basicops += 1
        
        while (j > 0) and (sortedarray[j] > x):
            
            sortedarray[j + 1] = sortedarray[j]
            j -= 1
            
            basicops += 2
                       
        sortedarray[j + 1] = x
        
    print(sortedarray)
    print(basicops, " operations")
    
    
    
arr = input_filename_to_array()



start = time.time()
insertion_sort_array(arr)
end = time.time()
#print(end - start)
