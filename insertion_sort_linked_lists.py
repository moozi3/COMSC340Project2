######################################
#Pyhton: Insertion sort using linked lists
#By: Louis Sader
#Class: COMSC340 Analysis of Algorithm
#Date: 15 March 2023
#This code usese the inerstion sort algorithm to sort the  
#elements of the list in ascending order 
######################################
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node
    
    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=' ')
            curr_node = curr_node.next
        print()
    
    def insertion_sort(self):
        if self.head is None:
            return
        
        sorted_list = LinkedList()
        curr_node = self.head
        while curr_node is not None:
            next_node = curr_node.next
            sorted_list.insert_sorted(curr_node.data)
            curr_node = next_node
        
        self.head = sorted_list.head
    
    def insert_sorted(self, data):
        new_node = Node(data)
        if self.head is None or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None and curr_node.next.data < data:
                curr_node = curr_node.next
            new_node.next = curr_node.next
            curr_node.next = new_node



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

    # Sort the linked list using insertion sort
    linked_list.insertion_sort()

    # Print the sorted list
    print("Sorted list:")
    linked_list.print_list()
