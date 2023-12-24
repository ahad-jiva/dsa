class Node:
    '''Node for use with doubly-linked list'''

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.head == self.head.prev

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance.  Assume that all items added to your 
           list can be compared using the < operator and can be compared for equality/inequality.
           Make no other assumptions about the items in your list'''
        n = Node(item)
        current = self.head.next
        while current != self.head:
            if n.item == current.item:
                return False
            elif current.item < n.item:
                current = current.next
            else:
                break
        n.next = current
        current.prev.next = n
        n.prev = current.prev
        current.prev = n
        return True

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
           returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        current = self.head.next
        while current != self.head:
            if current.item != item:
                current = current.next
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
        return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        index = 0
        current = self.head.next
        while current != self.head:
            if current.item == item:
                return index
            else:
                current = current.next
                index += 1
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        current = self.head.next
        i = -1
        if index < 0:
            raise IndexError
        else:
            while current != self.head:
                i += 1
                if i == index:
                    removed = current.item
                    self.remove(removed)
                    return removed
                current = current.next
            raise IndexError

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.search_helper(item, self.head.next)

    def search_helper(self, item, node):
        while node != self.head:
            if node.item == item:
                return True
            else:
                return self.search_helper(item, node.next)
        return False

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        output_list = []
        current = self.head.next
        for i in range(self.size()):
            output_list.append(current.item)
            current = current.next
        return output_list

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.python_list_reversed_helper([], self.head.prev)

    def python_list_reversed_helper(self, rev_list, node):
        while node != self.head:
            return self.python_list_reversed_helper(rev_list + [node.item], node.prev)
        return rev_list

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.head.next)

    def size_helper(self, node):
        if node == self.head:
            return 0
        return 1 + self.size_helper(node.next)
