class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None 





class LinkedList:

    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    # this is exactly why we like linked lists / O(1)
    def insert_start(self, data):

        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node


    # linear running time O(N)
    def insert_end(self, data):
        
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
        print("Insert End: ")
        print("New Node: ", new_node)
        print("-------------")
        actual_node = self.head
        print("Actual Node: ")
        print(hex(id(actual_node)))

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode
        
        actual_node.nextNode = new_node
    

    def remove(self, data):
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode

        # search miss - the itme is not present in the linked list
        if actual_node is None:
            return

        self.numOfNodes = self.numOfNodes -1 
        if previous_node is None:
            self.head = actual_node.nextNode
        else:
            previous_node.nextNode = actual_node.nextNode

    def size_of_list(self):
        return self.numOfNodes

    # O(N)
    def traverse(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode



linked_list = LinkedList()
linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_end(10)
linked_list.insert_end(20)
linked_list.insert_end(30)




