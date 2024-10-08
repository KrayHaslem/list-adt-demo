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

            # Remove Remaining values over length
            for i in range(self.length, self.allocation_size):
                self.array[i] = None

    def sort(self):
        self.array.sort(key=lambda element: (element is None, element))
        # Key happens to the element before sorting, .sort cannot handle none values,
        # so this creates tuples to sort, (element is None, element), for none 1 and
        # others 0, then the sort puts all of the none values to the end as True (1)
        # is greater than false(0) and the other elements get sorted normally based on
        # thier values existing in the second position on the tuple.

    def merge_sort(self):  # chatGPT replacement for sort after multiple attempts and slight modification
        def merge(left, right):
            merged = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] is None:
                    merged.append(left[i])
                    i += 1
                elif right[j] is None:
                    merged.append(right[j])
                    j += 1
                elif left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        # Start with a width of 1 and double the width each iteration
        width = 1
        n = len(self.array)
        while width < n:
            for i in range(0, n, 2 * width):
                left = self.array[i:i + width]
                right = self.array[i + width:i + 2 * width]
                self.array[i:i + 2 * width] = merge(left, right)
            width *= 2

        # Insert None values to the end of the list
        self.array = [x for x in self.array if x is not None] + [None] * (self.allocation_size - self.length)
