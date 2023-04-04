#@Author: Hirwa Ishimwe
# Node and Linked List classes by @Louis Sader
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
        basic_ops = 1
        if self.head is None:
            return
        
        basic_ops += 2
        curr_node = self.head.next
        self.head.next = None
        while curr_node is not None:
            next_node = curr_node.next
            basic_ops += 1
            if curr_node.data < self.head.data:
                curr_node.next = self.head
                self.head = curr_node
                basic_ops += 3
            else:
                prev_node = self.head
                while prev_node.next is not None and prev_node.next.data < curr_node.data:
                    prev_node = prev_node.next
                    basic_ops += 2
                curr_node.next = prev_node.next
                prev_node.next = curr_node
                basic_ops += 4
            curr_node = next_node
            basic_ops += 1
        return basic_ops
    
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

# Main method
if __name__ == '__main__':

    data_files = ["inorder5k.txt","rev5k.txt","random5k.txt","inorder10k.txt",
                  "rev10k.txt","random10k.txt","inorder100k.txt",
                    "rev100k.txt","random100k.txt"]
    #loop to record basic operations for each file
    for file in data_files:
        linked_list = parse_data_file("datafiles/" + file)
        result = linked_list.insertion_sort()
        print(f"Insertion Sorting {file} took: {result} Basic Operations")