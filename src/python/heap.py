

class Heap():

    def __init__(self):
        self.heap = []

    # takes an unsorted arr and moves them until all nodes satisfy the heap property
    def buildHeap(self, arr):
        pass
    
    def peek(self):
        return self.heap[0]
    
    def pop(self):
        pass

    def insert(self, element):
        self.heap.append(element)
        position = len(self.heap)-1
        self._siftUp(position)

    def _siftUp(self, pos):
        parent_idx = (pos-1) // 2
        
        if parent_idx < 0:
            return

        if self.heap[parent_idx] < self.heap[pos]:
            self._swap(parent_idx, pos)
        
        self._siftUp(parent_idx)

    def _siftDown(self, pos):
        pass


    def _swap(self, i1, i2):
        temp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = temp


input_arr = [4,2,1,6,8,9,2,4,5]

heap = Heap()
heap.insert(1)
heap.insert(3)
heap.insert(10)
heap.insert(34)
heap.insert(17)
heap.insert(12)

print(heap.heap)
