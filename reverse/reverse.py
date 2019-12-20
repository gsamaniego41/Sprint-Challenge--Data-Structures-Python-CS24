class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        # to iterate sll, start from the head
        current = self.head
        prev = None

        while current != None:
            print(current.value)
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
            # prev, current = current, next_node
        self.head = prev

# example list = [1,2,3,4,5]
# First iteration:
# current = 1
# prev = None
  # next_node = 2 (saves 2 on the side, leaving its spot open)
  # current.next_node = None takes 2's place
  # prev = current (saves 1 on the side, leaving its spot open)
  # current = 2 (2 takes 1's place)
  # ---- Repeat until current is None ----
# When current is None
  # 5 is its prev
  # set 5 as the new head
  # list is reversed!


mylist = LinkedList()
mylist.add_to_head(1)
mylist.add_to_head(2)
mylist.add_to_head(3)
mylist.add_to_head(4)
mylist.add_to_head(5)
print(mylist.reverse_list())
