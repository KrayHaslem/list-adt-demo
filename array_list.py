class ArrayList:
    def __init__(self, capacity=10):
        self.array = [None] * capacity
        self.allocation_size = capacity
        self.length = 0

    def append(self, new_item):
        # resize() if the array is full
        if self.allocation_size == self.length:
            self.resize(self.length * 2)

        # Insert the new item at index equal to self.length
        self.array[self.length] = new_item

        # Increment the array's length
        self.length = self.length + 1

    def resize(self, new_allocation_size):
        # Create a new array with the indicated size
        new_array = [None] * new_allocation_size

        # Copy items in current array into the new array
        for i in range(self.length):
            new_array[i] = self.array[i]

        # Assign the array data member with the new array
        self.array = new_array

        # Update the allocation size
        self.allocation_size = new_allocation_size

    def prepend(self, new_item):
        # resize() if the array is full
        if self.allocation_size == self.length:
            self.resize(self.length * 2)

        # Shift all array items to the right,
        # starting from the last index and moving
        # down to the first index.
        for i in reversed(range(1, self.length+1)):
            self.array[i] = self.array[i-1]

        # Insert the new item at index 0
        self.array[0] = new_item

        # Update the array's length
        self.length = self.length + 1

    def insert_after(self, index, new_item):
        # resize() if the array is full
        if self.allocation_size == self.length:
            self.resize(self.length * 2)

        # Shift all the array items to the right,
        # starting from the last item and moving down to
        # the item just past the given index.
        for i in reversed(range(index+1, self.length+1)):
            self.array[i] = self.array[i-1]

        # Insert the new item at the index just past the
        # given index.
        self.array[index+1] = new_item

        # Update the array's length
        self.length = self.length + 1

    def search(self, item):
        # Iterate through the entire array
        for i in range(self.length):
            # If the current item matches the search
            # item, return the current index immediately.
            if self.array[i] == item:
                return i

        # If the above loop finishes without returning,
        # it means the search item was not found.
        return -1

    def remove_at(self, index):
        # Make sure the index is valid for the current array
        if index >= 0 and index < self.length:
            # Shift items from the given index up to the
            # end of the array.
            for i in range(index, self.length-1):
                self.array[i] = self.array[i+1]

            # Update the array's length
            self.length = self.length - 1

    def sort(self):
        self.array.sort(key=lambda element: (element is None, element))
        # Key happens to the element before sorting, .sort cannot handle none values,
        # so this creates tuples to sort, (element is None, element), for none 1 and
        # others 0, then the sort puts all of the none values to the end as True (1)
        # is greater than false(0) and the other elements get sorted normally based on
        # thier values existing in the second position on the tuple.
