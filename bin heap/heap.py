class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.capacity = capacity
        self.heap = [None] * (capacity + 1)
        self.size = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        # Should call perc_up
        if self.is_full():
            return False
        self.heap[self.size + 1] = item
        self.size += 1
        self.perc_up(self.size)
        return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        return self.heap[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        # Should call perc_down
        if self.is_empty():
            return None
        max_item = self.heap[1]
        last_item = self.heap[self.size]
        self.heap[1] = last_item
        self.heap[self.size] = None
        self.perc_down(1)
        self.size -= 1
        return max_item

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.heap[1:self.size+1]

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        # Bottom-Up construction.  Do NOT call enqueue
        self.capacity = max(self.capacity, len(alist))
        self.heap = [None] * (self.capacity + 1)
        for i in range(len(alist)):
            self.heap[i+1] = alist[i]
            self.size += 1
        start = self.size//2
        for j in range(start, 0, -1):
            self.perc_down(j)

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.size == 0

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.size == self.capacity

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        to_be_moved = i
        left = 2 * i
        right = (2 * i) + 1
        if right <= self.size and self.heap[right]:
            max_child = max(self.heap[left], self.heap[right])
            max_child_index = None
            if max_child == self.heap[left]:
                max_child_index = left
            elif max_child == self.heap[right]:
                max_child_index = right
            if self.heap[to_be_moved] < max_child:
                self.heap[to_be_moved], self.heap[max_child_index] = self.heap[max_child_index], self.heap[to_be_moved]
                self.perc_down(max_child_index)
        elif left <= self.size and self.heap[left]:
            if self.heap[to_be_moved] < self.heap[left]:
                self.heap[to_be_moved], self.heap[left] = self.heap[left], self.heap[to_be_moved]
                self.perc_down(left)

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        if (i // 2) > 0:
            if self.heap[i // 2] < self.heap[i]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
                self.perc_up(i // 2)

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.heap = [None] * (self.capacity + 1)
        self.build_heap(alist)
        for i in range(len(alist)-1, -1, -1):
            alist[i] = self.dequeue()


