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
        if self.storage.__len__() > self.capacity:
            self.storage.add_to_head(item)
        else:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)

        # if full capacity, replace

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # num = 0
        # while num < self.storage.__len__():
        #     current_head = self.storage.head
        #     list_buffer_contents.append(current_head.value)
        #     self.storage.move_to_end(current_head)
        #     num += 1

        # for i in self.storage.__len__():
        #     print(i)
        #     if i is not None:
        #         list_buffer_contents.append(i)

        return list_buffer_contents


buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())


# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
