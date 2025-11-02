class EmptyHeapException(Exception):
    def __init__(self, msg='Empty Heap'):
        self.msg = msg
    def __str__(self):
        return self.msg


class Heap:
    def __init__(self):
        self.heap = []

    def createHeap(self, list1):  # fixed: use correct parameter name
        for e in list1:
            self.insert(e)

    def insert(self, e):
        index = len(self.heap)
        parentIndex = (index - 1) // 2
        while index > 0 and self.heap[parentIndex] < e:
            if index == len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index] = self.heap[parentIndex]
            index = parentIndex
            parentIndex = (index - 1) // 2
        if index == len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index] = e

    def top(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        return self.heap[0]

    def delete(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        temp = self.heap.pop()  # take last element
        index = 0

        while True:
            leftChildIndex = 2 * index + 1
            rightChildIndex = 2 * index + 2
            if leftChildIndex >= len(self.heap):
                break

            # find larger child
            if rightChildIndex < len(self.heap) and self.heap[rightChildIndex] > self.heap[leftChildIndex]:
                largerChildIndex = rightChildIndex
            else:
                largerChildIndex = leftChildIndex

            if self.heap[largerChildIndex] > temp:
                self.heap[index] = self.heap[largerChildIndex]
                index = largerChildIndex
            else:
                break

        # place temp in its correct position
        if index < len(self.heap):
            self.heap[index] = temp
        else:
            self.heap.append(temp)

        return max_value

h = Heap()
h.createHeap([3, 10, 5, 6, 2, 8])
print("Heap:", h.heap)
print("Top:", h.top())
print("Deleted:", h.delete())
print("Heap after delete:", h.heap)
