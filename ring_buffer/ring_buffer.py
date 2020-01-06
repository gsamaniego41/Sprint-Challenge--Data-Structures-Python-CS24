from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # When a new element is inserted,
    # the oldest element in the ring buffer is
    # overwritten with the newest element

    def append(self, item):
        # self.current = item
        # keep adding to tail until max capacity
        # if max capacity, replace head with item
        print('capacity:', self.capacity)
        print('length:', self.storage.__len__())

        if self.storage.__len__() > self.capacity:
            print('max capacity')
            self.storage.delete(self.storage.head)
            self.storage.head = item
        else:
            print(item)
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        current = self.storage.head
        # next_node = current.next

        for _ in range(self.storage.__len__()):
            # print('current next', current.next)
            if current is not None:
                # print('current -->', current)
                list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents


# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')
# buffer.append('e')

# print(buffer.get())


# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
