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

import time
  

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
        
    for i in range(n):
        x = arr[i]
        j = i - 1
        
        while (j > 0) and (sortedarray[j] > x):
            
            sortedarray[j + 1] = sortedarray[j]
            j -= 1
                       
        sortedarray[j + 1] = x
        
'''
# This method uses the file name and parses the values in the file into an array
'''
def parse_data_file(file):
    #a list to store the numbers from the file
    data_array = []
    with open(file, "r") as open_file:
        # read each line and add it to the list as an integer
        line = open_file.readline().strip()
        data_array.append(int(line))
        while line:
            line = open_file.readline().strip()
            if line != '':
                data_array.append(int(line))
        #return the lit
    return data_array
    
#Main method
if __name__ == '__main__':

    #list of the file to run
    data_files = ["inorder5k.txt","rev5k.txt","random5k.txt","inorder10k.txt",
                  "rev10k.txt","random10k.txt","inorder100k.txt",
                    "rev100k.txt","random100k.txt"]
    # loop to record the time for sorting each file 
    for file in data_files:
        data = parse_data_file("datafiles/" + file)
        start = time.time()
        insertion_sort_array(data)
        end = time.time()
        result = end - start
        print(f"Insertion Sorting an array of {file} took: {end - start:.10f} seconds")
    