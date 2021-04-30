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


    def add(self, data):

        """
        Adds new Node containing data at head of the list

        Has O(1) - constant runtime

        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


    def search(self, key):

        """
        Search for first node containing data that matches the key
        Return the node or 'None' if not found

        Takes O(n) - linear runtime
        """
        current = self.head

        while current != None:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):

        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding the node at the insertion point takes O(n) runtime

        Takes overall O(n) runtime
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position = position - 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None if key doesnt exist
        Takes 0(n) - linear runtime
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current



    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) - linear runtime
        """
        
        nodes = []
        current = self.head

        while current != None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '->'.join(nodes)

