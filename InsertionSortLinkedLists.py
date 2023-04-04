######################################
#Pyhton: Insertion sort using linked lists
#By: Louis Sader
#Class: COMSC340 Analysis of Algorithm
#Date: 15 March 2023
#This code usese the inerstion sort algorithm to sort the  
#elements of the list in ascending order 
######################################
import time

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=' ')
            curr_node = curr_node.next
        print()
    
    def insertion_sort(self):
        if self.head is None:
            return
        
        curr_node = self.head.next
        self.head.next = None
        while curr_node is not None:
            next_node = curr_node.next
            if curr_node.data < self.head.data:
                curr_node.next = self.head
                self.head = curr_node
            else:
                prev_node = self.head
                while prev_node.next is not None and prev_node.next.data < curr_node.data:
                    prev_node = prev_node.next
                curr_node.next = prev_node.next
                prev_node.next = curr_node
            curr_node = next_node

# Method to get the data from a file adn return a linked list
def parse_data_file(file):
    linked_list = LinkedList()
    with open(file, "r") as open_file:
        line = open_file.readline().strip()
        linked_list.insert(int(line))
        while line:
            line = open_file.readline().strip()
            if line != '':
                linked_list.insert(int(line))
    return linked_list


if __name__ == '__main__':

    # list of the data files
    data_files = ["inorder5k.txt","rev5k.txt","random5k.txt","inorder10k.txt","rev10k.txt","random10k.txt","inorder100k.txt",
                    "rev100k.txt","random100k.txt"]
    
    # loop through files and get their times
    for file in data_files:
        linked_list = parse_data_file("datafiles/" + file)
        start_time = time.time()
        linked_list.insertion_sort()
        end_time = time.time()
        print(f"Insertion Sorting a linked list of {file} took: {end_time - start_time:.10f} seconds")
