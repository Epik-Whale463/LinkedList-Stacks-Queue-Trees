# linnked list implementation


class Node:
    """
    An object for storing a single node of a linked list 
    Models two attributes - data and the link to the next node in the list
    
    """
    data  = None
    next_node = None
    
    def __init__(self,data):
        self.data = data
        
    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    """
    Singly linked list
    
    """
    
    def __init__(self):
        self.head = None
        
    
    def is_empty(self):
        return self.head ==None
    
    
    def size(self):
        """
        Returns the number of nodes in the list - takes linear run time
        """
        current  = self.head
        count = 0
        
        while current: # till current is not empty
            count +=1
            current = current.next_node
        return count
    
    
    def add(self,data):
        """
        Adds a new node containing data at the head of the list - takes constant time 
        """
        new_node  = Node(data) # create a new node to add to the linked list
        
        new_node.next_node = self.head # point the new node's 'next' property to the current head node of the list
        
        self.head  = new_node # make the new_node as the head of the list 
        
       
    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Reutrns the node or None if not found
        Takes O(n) - linear time to implement
        """
        current  = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return f"Key not found"
    
    
    def insert(self, data, index):
        """
        Inserts a new node at the given index
        Insertion takes constant time but finding the node at the given index takes linear time
        Takes O(n) time overall
        """
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            new.next_node = next_node
            prev_node.next_node = new
            
                
    def remove(self, key):
        """
        Removes Node containing data that matches the given key
        and returns None or Node , if the key is not found
        Takes O(n) time to implement
        """
        current  = self.head
        previous = None
        
        found = False
        
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head  = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
    
        return current
    
    
    def node_at_index(self,index):
        if index == 0:
            return self.head
        else:
            current  = self.head
            position = 0
            
            while position < index:
                current = current.next_node
                position +=1
            
            return current
        
        
    
    def __repr__(self):
        """
        Returns a string representation of the list 
        Takes O(n) time 
        """
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        
        return '->'.join(nodes)
    
    