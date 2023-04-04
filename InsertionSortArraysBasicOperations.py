# -*- coding: utf-8 -*-
# @author: moozi

#Insertion sort method
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
    sortedarray= arr
    
    n = len(arr)
    i = 2
    #initialize the basic operations counter
    basicops = 0   
    
    for i in range(n):
        x = arr[i]
        #increment for assignment
        basicops += 1
        j = i - 1        
        while (j > 0) and (sortedarray[j] > x):
            
            sortedarray[j + 1] = sortedarray[j]
            j -= 1
            #increment for comparisons in while conditionals
            basicops += 2
                       
        sortedarray[j + 1] = x
        #increment for assignment
        basicops += 1
    return basicops


# This method uses the file name and parses the values in the file into an array  
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
    # loop to record the basic operations for sorting each file 
    for file in data_files:
        data = parse_data_file("datafiles/" + file)
        result = insertion_sort_array(data)
        print(f"Insertion Sorting {file} took: {result} Basic Operations")