
class Node:
    """
    Creates nodes to be added to the Linked List
    """

    def __init__(self, value, next_ = None):
        self.value = value
        self.next_ = next_

class Linkedlist:
    """
    Starts as an empty list, then nodes can be added or removed from it
    """

    def __init__(self):
        self.head = None
    

    def insert(self, value):
        """
        Inserts a node at the beggining of the list
        """

        node = Node(value)

        if self.head:
            node.next_ = self.head
        
        self.head = node
        

ll = Linkedlist()
ll.insert(5)



print(ll.head.value)




