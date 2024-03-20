class PriorityQueue:
    def __init__(self) -> None:
        self._heap: list = []
        self._next_id: int = 1
    
    @property
    def heap(self):
        return self._heap

    @heap.setter
    def heap(self, list):
        self._heap = list
        
    @property
    def next_id(self):
        return self._next_id
    
    @next_id.setter
    def next_id(self, id):
        self._next_id = id
        
    
    def __repr__(self) -> str:
        return repr(self.heap)

    def display(self) -> None:
        for i in self.heap:
            print(i)

    def get_next_id(self) -> int:
        id: int = self.next_id
        self.next_id += 1
        return id
    
    def parent(self, index: int) -> int:
        return (index - 1) // 2
    
    def left_child(self, index: int) -> int:
        return 2 * index  + 1

    def right_child(self, index: int) -> int:
        return 2 * index  + 2
    
    def swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def enqueue(self, item: str, priority: int) -> None:
        new_node: tuple = (self.get_next_id(), item, priority)
        self.heap.append(new_node)
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_up(self, index: int) -> None:
        while index > 0 and self.heap[index][2] > self.heap[self.parent(index)][2]:
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    def dequeue(self) -> tuple:
        if self.is_empty():
            raise IndexError("Queue is empty")
        self.swap(0, len(self.heap) - 1)
        item: tuple = self.heap.pop()
        self.heapify_down(0)
        return item
    
    def heapify_down(self, index: int) -> None:
        while self.left_child(index) < len(self.heap):
            biggest_child: int = self.get_biggest_child(index)
            if self.heap[index][2] < self.heap[biggest_child][2]:
                self.swap(index, biggest_child)
                index = biggest_child
            elif self.heap[index][2] == self.heap[biggest_child][2]:
                if self.heap[index][0] > self.heap[biggest_child][0]:
                    self.swap(index, biggest_child)
                    index = biggest_child
                else:
                    break
            else:
                break
    
    def get_biggest_child(self, index: int) -> int:
        left_child_index: int = self.left_child(index)
        right_child_index: int = self.right_child(index)

        if right_child_index < len(self.heap):
            # Compare priorities
            if self.heap[right_child_index][2] > self.heap[left_child_index][2]:
                return right_child_index
            elif self.heap[right_child_index][2] == self.heap[left_child_index][2]:
                # compare which item got put first into the heap
                if self.heap[right_child_index][0] < self.heap[left_child_index][0]:
                    return right_child_index
                else:
                    return left_child_index
            else:
                return left_child_index
        else:
            return left_child_index
    
    def is_empty(self) -> bool:
        return len(self.heap) == 0
        
if __name__ == "__main__":
    pq: PriorityQueue = PriorityQueue()
    pq.enqueue('D1', 0)
    pq.enqueue('D2', 0)
    pq.enqueue('D3', 0)
    pq.enqueue('D4', 0)
    pq.enqueue('P1', 5)
    pq.enqueue('P2', 5)
    pq.enqueue('P3', 5)
    pq.enqueue('P4', 4)
    pq.enqueue('P11', 12)
    pq.enqueue('P41', 23)

    pq.display()

    print(f' dequeued: {pq.dequeue()}') 
    print(f' dequeued: {pq.dequeue()}') 
    print(f' dequeued: {pq.dequeue()}') 
    print(f' dequeued: {pq.dequeue()}') 
    print(f' dequeued: {pq.dequeue()}') 
    print(f' dequeued: {pq.dequeue()}') 
    print()
    pq.display()
    print()
    print(f' dequeued: {pq.dequeue()}') 
    print(f' dequeued: {pq.dequeue()}') 
    print(f' dequeued: {pq.dequeue()}') 
    print(f' dequeued: {pq.dequeue()}') 
