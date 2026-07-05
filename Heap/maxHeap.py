class maxHeap:
  def __init__(self):
    self.heap=[]
    
  def parent(self,ind):
    return (ind-1)//2
  
  def left(self,ind):
    return 2*ind+1
  
  def right(self,ind):
    return 2*ind+2
  
  def insert(self,key):
    self.heap.append(key)
    ind=len(self.heap)-1
    while ind > 0:
      parent =self.parent(ind)
      if self.heap[parent] > self.heap[ind]:
        break
      self.heap[parent],self.heap[ind] = self.heap[ind],self.heap[parent]
      ind=parent
      
  def extractMax(self):
    if len(self.heap) == 0:
      return None
    if len(self.heap) == 1:
      return self.heap.pop()
    root = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.heapify(0)
    return root
  
  def heapify(self,ind):
    largest=ind
    left=self.left(ind)
    right=self.right(ind)
    if left < len(self.heap) and self.heap[left] > self.heap[largest]:
      largest=left
    if right < len(self.heap) and self.heap[right] > self.heap[largest]:
      largest=right
    if largest != ind:
      self.heap[largest],self.heap[ind] = self.heap[ind],self.heap[largest]
      self.heapify(largest)
      
heap=maxHeap()
heap.insert(15)
heap.insert(40)
heap.insert(20)
heap.insert(30)
heap.insert(50)
print(heap.heap)