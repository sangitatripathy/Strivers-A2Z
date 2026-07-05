class minHeap:
  def __init__(self):
    self.heap=[]

  def parent(self,index):
    return (index-1)//2

  def left(self,index):
    return 2*index+1

  def right(self,index):
    return 2*index+2

  def insert(self,key):
    self.heap.append(key)
    ind=len(self.heap)-1
    while ind > 0:
      parent = self.parent(ind)
      if self.heap[parent] <= self.heap[ind]:
        break
      self.heap[parent],self.heap[ind] = self.heap[ind],self.heap[parent]
      ind=parent

  def extractMin(self):
    if len(self.heap) == 0:
      return None
    if len(self.heap) == 1:
      return self.heap.pop()
    root = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.heapify(0)
    return root

  def heapify(self,index):
    smallest = index
    left = self.left(index)
    right = self.right(index)
    if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
      smallest=left
    if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
      smallest= right
    if smallest != index:
      self.heap[smallest],self.heap[index] = self.heap[index],self.heap[smallest]
      self.heapify(smallest)
      
heap=minHeap()
heap.insert(10)
heap.insert(4)
heap.insert(15)
heap.insert(2)
heap.insert(20)
heap.insert(1)
print(heap.heap)
heap.extractMin()
print(heap.heap)