class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
        self.prev = None  # Not used for singly linked lists double linked only
