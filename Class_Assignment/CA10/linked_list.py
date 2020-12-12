# Define a class for the linked list
from node import Node

# Class for a simple Linked List

class LinkedList:
    def __init__(self, data):
        self.start_node = Node(data)


    def traverse_list(self):
        temp = self.start_node
        print("linked list is : ",end=" ")
        if temp == None:
            print("the linked is empty")
        else:    
            while temp is not None:
                print(temp.data, end=' -> ')
                temp = temp.next
        print("")

    def insert_at_start(self, data):
        temp = Node(data)
        temp.next = self.start_node
        self.start_node = temp


    def insert_at_end(self, data):
        new_node=Node(data)
        if self.start_node is None :  #check if the linked list is empty or not # the list is empty
            self.start_node=new_node #set the value of the start_node variable to new_node object.
            return
        temp=self.start_node #initialize a variable n with the start node.
        while temp.next is not None : #the list already contains some nodes
            temp = temp.next #set the reference of the last node to the newly created new_node.
        temp.next=new_node
    
    def insert_after(self, x, data):
        new_node = Node(data)
        temp = self.start_node
        
        while temp is not None:
            if temp.data ==  x:   
                temp2 = temp.next
                temp.next = new_node
                new_node.next = temp2
                return
            else:
                temp = temp.next
        print(f"item {x} is not found")    


    def insert_before_item(self, x, data):
        new_node = Node(data)
        temp1 = self.start_node
        temp2 = temp1.next

        if self.start_node == x:
            self.insert_at_start(data)

        while temp1 is not x:
            if temp2.data ==  x:   
                temp1.next = new_node
                new_node.next = temp2
                break
            else:
                temp1 = temp1.next
                temp2 = temp2.next
            print(f"item {x} is not found")  
        
    def insert_at_index (self, index, data):
        #new_node = Node(data)
        temp = self.start_node
        for i in range(index):
            temp = temp.next
        x=temp.data
        self.insert_before_item(x, data)    


    def get_count(self):
        count = 0
        temp=self.start_node 
        while temp:
            temp = temp.next
            count += 1
        return count

    def search_item(self, x):
        count = 0
        temp = self.start_node

        while temp is not None:
            if temp.data ==  x:   
                print(f"item {x} found at index {count}")
                return
            else:
                count +=1
                temp = temp.next

        print(f"item {x} is not found") 

    def make_new_list(self):        #not work
        current = self.start_node
        while current:
            prev = current.next
            del current.data
            current = prev

    def delete_at_start(self):
        temp = self.start_node.next
        del self.start_node
        self.start_node = temp

    def delete_at_end(self):        #not work
        temp = self.start_node
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def reverse_linkedlist(self):
        count = self.get_count()
        temp = self.start_node
        rev_linked_list = []
        
        for i in range(count):
            rev_linked_list.append(temp.data)
            temp = temp.next
        
        rev_linked_list.reverse()
        temp1 = self.start_node
        
        for i in range(0,count):
            temp1.data = rev_linked_list[i]
            temp1 = temp1.next
        

# Our linked list like this now
#   (40)->(10)->(5)->(3)-> None

my_list = LinkedList (3)
my_list.insert_at_start(2)
my_list.insert_after(2,4)
my_list.insert_after(3,5)
my_list.search_item(4)
my_list.delete_at_end()
my_list.delete_at_start()
my_list.traverse_list()

# my_list.reverse_linkedlist()
# my_list.traverse_list(start)

# print(my_list.get_count())