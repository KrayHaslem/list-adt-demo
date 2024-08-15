class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        print_node = self.head
        while print_node != None:
            print(print_node.data, end=' ')
            print_node = print_node.next

    def append(self, new_node):
        if self.head == None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:  # Add new node to tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node):
        if self.head == None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:  # Replace head
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head == None:  # Empty list
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:  # Replace tail
            self.tail.next = new_node
            self.tail = new_node
        else:  # Add to middle
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_after(self, current_node):
        # Special case, remove head
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self.head = succeeding_node
            if succeeding_node == None:  # Removed last item
                self.tail = None
        elif current_node.next != None:  # Current node is not tail
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None:  # Removed tail
                self.tail = current_node

    def insertion_sort_singly_linked(self):  # Less Efficient with lack of support for reverse traversal with no prev value
        before_current = self.head
        current_node = self.head.next
        while current_node != None:  # Traverse list until tail
            next_node = current_node.next
            position = self.find_insertion_position(current_node.data)
            if position == before_current:  # Current node correct position
                before_current = current_node
            else:  # Move current node
                self.remove_after(before_current)
                if position == None:  # Replace head with current node
                    self.prepend(current_node)
                else:  # Insert into position
                    self.insert_after(position, current_node)
            current_node = next_node

    def find_insertion_position(self, data_value):
        position_a = None
        position_b = self.head
        while (position_b != None) and (data_value > position_b.data):
            position_a = position_b
            position_b = position_b.next
        return position_a
