class Node: 	#Node Class definition
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None
	   
	   
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
 
 
class CircularDoublyLinkedList: #Creating the LinkedList
    def __init__(self):
        self.first = None
		self.__head = None
        self.__tail = None
        self.__size = 10

 
    def get_node(self, index): 
        current = self.first
        for i in range(index):
            current = current.next
            if current == self.first:
                return None
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node
 
    def insert_before(self, ref_node, new_node):
        self.insert_after(ref_node.prev, new_node)
 
    def insert_end(self, new_node):
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.first.prev, new_node)
 
    def insert_beginning(self, new_node):
        self.insert_end(new_node)
        self.first = new_node		
		
	def getIndex(self, index):
        current = self.__head
        c_index = 0
        for i in range(1,index):
            current = current.next
            c_index += 1
            if c_index == self.__size:
                c_index = 0
        return c_index
 
    def remove(self, node):
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.
			== node:
                self.first = node.next
 
	    
 
a_cdllist = CircularDoublyLinkedList()
 