# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:13:25 2023

@author: moozi

Lauren Moulaison
Date: 3/19/23
Class: COMSC340
Instructor: Cates

Description: sorts arrays by implementing insertion sort
"""
#let's get into it

"""
To create this code, I will create the actual insertion sort method, as well as
one method that takes in a file name to test the sort method, and one method that
parses the data into an array. There will also be lines that print the array  
before and after sorting to ensure the sorting method works correctly, simply
uncomment where needed.
"""
#define global pieces so they can be called in different functions
global arr, sortedarray

import time

"""
this method gathers the file name and parses the values in the file into an
array
"""
#Method for getting and parsing the input data into a list 
def parse_data_file(file):
    data_array = []
    with open(file, "r") as open_file:
        line = open_file.readline().strip()
        data_array.append(int(line))
        while line:
            line = open_file.readline().strip()
            if line != '':
                data_array.append(int(line))
    return data_array
    

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
    sortedarray = arr
    n = len(arr)
    for i in range(1, n):
        x = arr[i]
        j = i - 1
        while (j >= 0) and (sortedarray[j] > x):
            sortedarray[j + 1] = sortedarray[j]
            j -= 1
        sortedarray[j + 1] = x
    return sortedarray
        
 # Main        
if __name__ == '__main__':

    # list of the data files
    data_files = ["inorder5k.txt","inorder10k.txt","inorder100k.txt","rev5k.txt","rev10k.txt",
                    "rev100k.txt","random5k.txt","random10k.txt","random100k.txt"]
    
    # loop through files and get their times
    for file in data_files:
        arr = parse_data_file("datafiles/" + file)
        start_time = time.time()
        insertion_sort_array(arr)
        end_time = time.time()
        print(f"Insertion Sorting {file} took: {end_time - start_time:.10f} seconds")
