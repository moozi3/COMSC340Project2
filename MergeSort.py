# @author: Hirwa Ishimwe

import time

#Merge sort method
def merge_sort(arr):
    n = len(arr)
    
  #Split the array if its larger that 1 element
    if n > 1:
        middle = n//2
        first_half = arr[:middle]
        second_half = arr[middle:]
        merge_sort(first_half)
        merge_sort(second_half)

    #Merge step
        i = 0
        j = 0
        k = 0
        #While it has not reached the end of either of the array
        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                arr[k] = first_half[i]
                i += 1
            else:
                arr[k] = second_half[j]
                j += 1
            k += 1
        while i < len(first_half):
            arr[k] = first_half[i]
            i += 1
            k += 1
        while j < len(second_half):
            arr[k] = second_half[j]
            j += 1
            k += 1
    return arr

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

# Main Method
if __name__ == '__main__':

    #list of files to parse
    data_files = ["inorder5k.txt","inorder10k.txt","inorder100k.txt","rev5k.txt","rev10k.txt",
                  "rev100k.txt","random5k.txt","random10k.txt","random100k.txt"]
    
    # loop to record the time for merge sorting each file 
    for file in data_files:
        data = parse_data_file("datafiles/" + file)
        start_time = time.time()
        merge_sort(data)
        end_time = time.time()
        print(f"Merge Sorting {file} took: {end_time - start_time:.10f} seconds")