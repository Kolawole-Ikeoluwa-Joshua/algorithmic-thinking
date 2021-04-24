class Node:
    """
    An object for storing a single node of a linked list
    models two attributes
    1. data
    2. link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data


    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:

    """
    Singly linked list
    """

    """
        head attribute models the only node the list will have reference to
        
    """

    def __init__(self): # class constructor sets default value of head to none
        self.head = None  

    def is_empty(self): # method to check if list is empty
        return self.head == None


    # convenience method to calculate size of list
    """
    Returns the number of nodes in the list 
    Takes 0(n)- linear runtime
    """

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1 
            current = current.next_node

        return count


    
        