#Note: Almost all of the functions are originally belongs to Lecture Note and the Live coding.
class Node:
    """
    :pre: None
    :post: function is accessed
    :desc: a Node class
    """
    def __init__(self, item=None, link=None):
        """
        :pre: item and link are the paramenter
        :post: array is changed
        :desc: an initiated stage
        """
        self.item = item
        self.next = link

    def __iter__(self):
        """
        :pre: item is defined
        :post: every item is returned
        :desc: an iterator function
        """
        return self.item
    
    def get_next(self):
        """
        :pre: next is defined
        :post: next item is returned
        :desc: a get next function
        """
        return self.next

    def __str__(self):
        """
        :pre: item is defined
        :post: item is returned
        :desc: print with the form str
        """
        return str(self.item)

    def set_next(self, newnext):
        """
        :pre: newnext is defined
        :post: new next item is returned
        :desc: a get new next function
        """
        self.next = newnext

'''
def print_structure(node):
    while node is not None:
        print(node,end=' ')
        node = node.next
    print()
'''

class List:
    def __init__(self):
        """
        :pre: table size is the paramenter
        :post: None
        :desc: an initiated stage
        """
        self.head = None
        self.count = 0
        
    def __iter__(self):
        """
        :pre: None
        :post: self.head is returned
        :desc: an iterator function
        """
        return List(self.head)
    
    def is_empty(self):
        """
        :pre: None
        :post: self.count variable is definied
        :desc: set self.count to zero
        """
        return self.count == 0

    def is_full(self):
        """
        :pre: None
        :post: False is returned
        :desc: Cannot be full so return False
        """
        return False

    def reset(self):
        """
        :pre: None
        :post: init function is called
        :desc: Reset to the initial stage
        """
        self.head = None
        self.count = 0

    def __len__(self):
        """
        :pre: None
        :post: self.count is returned
        :desc: display length
        """
        return self.count

    def _get_node(self, index):
        """
        :pre: index is defined
        :post: node is returned
        :desc: get node function
        """
        assert 0 <= index < self.count, "Index out of bounds"
        node = self.head
        for _ in range(index):
            node = node.next
        return node
    '''
    def add(self, item):
        temp = self.head
        self.head = Node(item)
        self.head.next = temp

    def append(self,item):
        current = self.head
        if current:
            while current.get_next()!=None:
                current = current.get_next()
            current.set_next(Node(item))
        else:
            self.head = Node(item)
        self.count += 1
    '''

    def insert(self, index, item):
        """
        :pre: index, item
        :post: item is either updated or insert, else index = 0
        :desc: to insert item
        """
        if index < 0:
            index = 0
        elif index > len(self):
            index = len(self)
        if index == 0:
            self.head = Node(item, self.head)
        else:
            node = self._get_node(index-1)
            node.next = Node(item, node.next)
        self.count += 1

    def delete(self, index):
        """
        :pre: index
        :post: item with that index is either succefully deleted or index error
        :desc: to delete index
        """
        if self.is_empty():
            raise IndexError("The list is empty")
        if index < 0 or index >= len(self):
            raise IndexError("Index is out of range")
        if index == 0:
            self.head = self.head.next
        else:
            node = self._get_node(index-1)
            node.next = node.next.next
        self.count -= 1


if __name__ == "__main__":
    a_list = List()
    
