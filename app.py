from pause import pause
from node import Node
from linked_list import LinkedList
from double_linked_list import DoubleLinkedList
from array_list import ArrayList


### LINKED LIST###
node_a = Node(66)
node_b = Node(99)
node_c = Node(44)
node_d = Node(95)
node_e = Node(42)
node_f = Node(17)

num_list = LinkedList()

num_list.append(node_b)   # Add 99
num_list.append(node_c)   # Add 44, make the tail
num_list.append(node_e)   # Add 42, make the tail

num_list.prepend(node_a)  # Add 66, make the head

num_list.insert_after(node_c, node_d)  # Insert 95 after 44
num_list.insert_after(node_e, node_f)  # Insert 17 after tail (42)

# Output list
print('List after adding nodes:', end=' ')
num_list.print_list()

pause()  # Press enter to proceed with remove after.

num_list.remove_after(node_e)   # Remove the tail (17)
num_list.remove_after(None)     # Remove the head (66)


# Output final list
print('List after removing nodes:', end=' ')
num_list.print_list()

print()
pause()  # Press enter to proceed with remove after.

### DOUBLY LINKED LIST###

dl_node_a = Node(66)
dl_node_b = Node(99)
dl_node_c = Node(44)
dl_node_d = Node(95)
dl_node_e = Node(42)
dl_node_f = Node(17)

dl_num_list = DoubleLinkedList()

dl_num_list.append(dl_node_b)   # Add 99
dl_num_list.append(dl_node_c)   # Add 44, make the tail
dl_num_list.append(dl_node_e)   # Add 42, make the tail

dl_num_list.prepend(dl_node_a)  # Add 66, make the head

dl_num_list.insert_after(dl_node_c, dl_node_d)  # Insert 95 after 44
dl_num_list.insert_after(dl_node_e, dl_node_f)  # Insert 17 after tail (42)

# Output list
print('List after adding nodes:', end=' ')
dl_num_list.print_list()

pause()

dl_num_list.remove(dl_node_f)  # Remove the tail
dl_num_list.remove(dl_node_a)  # Remove the head


# Output final list
print('List after removing nodes:', end=' ')
dl_num_list.print_list()

print()
pause()

## Array List ADT ##

array_list = ArrayList(4)  # capacity of 4

print("Initial array")
print("Allocation size: %d, length: %d" % (array_list.allocation_size, array_list.length))
print(array_list.array)
pause()


for item in [99, 44, 42]:
    array_list.append(item)

array_list.prepend(66)

print("Full array")
print("Allocation size: %d, length: %d" % (array_list.allocation_size, array_list.length))
print(array_list.array)
pause()

array_list.insert_after(2, 95)
array_list.insert_after(4, 17)

print("List after adding values: ")
print("Allocation size: %d, length: %d" % (array_list.allocation_size, array_list.length))
print(array_list.array)

pause()

array_list.remove_at(0)
array_list.remove_at(4)

print("List after removing values")
print("Allocation size: %d, length: %d" % (array_list.allocation_size, array_list.length))
print(array_list.array)

print()
pause

## SORTING##

num_list.insertion_sort_singly_linked()
print("-- Linked after sort --")
num_list.print_list()

print()
pause()

dl_num_list.insertion_sort_doubly_linked()
print("-- Double Linked after sort --")
dl_num_list.print_list()

print()
pause()

array_list.sort()
print("-- Array after sort --")
print("Allocation size: %d, length: %d" % (array_list.allocation_size, array_list.length))
print(array_list.array)
