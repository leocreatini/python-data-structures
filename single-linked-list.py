class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous node is not in list.')
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # assume data is unique
    def delete_node(self, key):
        cur_node = self.head

        # account for deleting head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None  # deletes node
            return

        # else, iterate through
        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next

        # account for key not found
        if cur_node is None:
            return

        # set node prior to deleted to its node after
        # if deleting 2 in 1, 2, 3, then set 1's next to 3.
        prev_node.next = cur_node.next
        cur_node = None  # then delete designated node

    def delete_index(self, index):
        pos = 0
        cur_node = self.head

        if pos is index:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        while cur_node and pos is not index:
            pos += 1
            prev_node = cur_node
            cur_node = cur_node.next

        # account for out of bounds to ensure loop ends
        if cur_node is None:
            print(f'Position "{index}" does not exist.')
            return

        # found index, link prev_nodeious to index-node's next, then delete index-node.
        prev_node.next = cur_node.next
        cur_node = None

    def len(self):
        count = 0
        cur_node = self.head
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)


linked_list = LinkedList()
linked_list.append(1)  # 1
linked_list.append(2)  # 1, 2
linked_list.append(3)  # 1, 2, 3
linked_list.append(4)  # 1, 2, 3, 4

# insert after the second node
linked_list.insert_after_node(linked_list.head.next, 5)  # 1, 2, 5, 3, 4

linked_list.delete_node(3)  # 1, 2, 5, 4
linked_list.delete_index(4)  # 1, 2, 5, 4  => error message
linked_list.delete_index(0)  # 2, 5, 4
linked_list.delete_index(2)  # 2, 5
print(f'Iterative count: {linked_list.len()}')  # print 2
# print 2
print(f'Recursive count: {linked_list.len_recursive(linked_list.head)}')

linked_list.print_list()
