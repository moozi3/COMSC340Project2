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
            
            basicops += 3
                       
        sortedarray[j + 1] = x
        basicops += 1
    return basicops
    
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
  
if __name__ == '__main__':

    data_files = ["inorder5k.txt","rev5k.txt","random5k.txt","inorder10k.txt",
                  "rev10k.txt","random10k.txt","inorder100k.txt",
                    "rev100k.txt","random100k.txt"]
    
    for file in data_files:
        data = parse_data_file("datafiles/" + file)
        result = insertion_sort_array(data)
        print(f"Insertion Sorting {file} took: {result} Basic Operations")