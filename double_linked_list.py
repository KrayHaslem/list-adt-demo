class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        print_node = self.head
        while print_node != None:  # Iterates each node with space afterwards
            print(print_node.data, end=' ')
            print_node = print_node.next

    def append(self, new_node):
        if self.head == None:  # Empty List
            self.head = new_node
            self.tail = new_node
        else:  # New node becomes tail
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, new_node):
        if self.head == None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:  # New node becomes head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head == None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            successor_node = current_node.next
            new_node.next = successor_node
            new_node.prev = current_node
            current_node.next = new_node
            if self.tail is current_node:
                self.tail = new_node
            else:
                successor_node.prev = new_node

    def remove(self, current_node):
        predecessor_node = current_node.prev
        successor_node = current_node.next

        if current_node is self.head:
            self.head = successor_node
        else:
            predecessor_node.next = successor_node

        if current_node is self.tail:  # update tail
            self.tail = predecessor_node
        else:
            successor_node.prev = predecessor_node

    def insertion_sort_doubly_linked(self):
        current_node = self.head.next  # second element in list
        while current_node != None:
            next_node = current_node.next
            search_node = current_node.prev

            # Traverses list in reverse to until search node becomes smaller than current node or reaches heas and becomes null
            while ((search_node != None) and
                   (search_node.data > current_node.data)):
                search_node = search_node.prev

            # Remove current node
            self.remove(current_node)

            # Reinsert current node
            if search_node == None:  # Smaller than current head
                current_node.prev = None
                self.prepend(current_node)
            else:  # inserts after found smaller node
                self.insert_after(search_node, current_node)

            # Advance to next node
            current_node = next_node
