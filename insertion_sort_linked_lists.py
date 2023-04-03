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


if __name__ == '__main__':
    # Creates a linked list object
    linked_list = LinkedList()

    # Insert some elements into the linked list
    linked_list.insert(3)
    linked_list.insert(1)
    linked_list.insert(4)
    linked_list.insert(2)
    linked_list.insert(5)

    # Print the original list
    print("Original list:")
    linked_list.print_list()

    # Time the sorting process
    start_time = time.time()
    linked_list.insertion_sort()
    end_time = time.time()

    # Print the sorted list
    print("Sorted list:")
    linked_list.print_list()

    # Print the time taken for sorting
    print(f"Time taken: {end_time - start_time} seconds")
