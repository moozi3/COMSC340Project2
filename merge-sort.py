# @author: Hirwa Ishimwe

#Merge sort method
def merge_sort(arr):
    #Get the length of the array
    n = len(arr)
    
  #Split the array if its larger that 1 element
    if n > 1:
        middle = n//2
        #copy first half of the array
        first_half = arr[:middle]
        #copy second half of the aray
        second_half = arr[middle:]
        #recursive split the arrays until they are only in 1 element in size
        merge_sort(first_half)
        merge_sort(second_half)

    #Merge step
        #Index of the first half array
        i = 0
        #Index of the second half array
        j = 0
        #index of the merged array
        k = 0
        #While it has not reached the end of either of the array
        while i < len(first_half) and j < len(second_half):
            #If the element if the first array index is lower add that to the merged array and increment its index
            if first_half[i] < second_half[j]:
                arr[k] = first_half[i]
                i += 1
            else:
                arr[k] = second_half[j]
                j += 1
            k += 1
        #If the first half's elements were not fully parsed and the rest of its elements to the sorted/emerged array
        while i < len(first_half):
            arr[k] = first_half[i]
            i += 1
            k += 1
        #If the second half's elements were not fully parsed and the rest of its elements to the sorted/emerged array
        while j < len(second_half):
            arr[k] = second_half[j]
            j += 1
            k += 1
        #return the sorted and merged array
    return arr

#Method for getting and parsing the input data into a list 
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

# Main Method
if __name__ == '__main__':
    #Ask the user to enter the file with data, collect the data from the file and merge sort it
    print(merge_sort(parse_data_file(input("Enter the data file: "))))