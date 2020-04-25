# class for Node with data and priority
class Node:
  
  def __init__(self, info, priority):
    self.info = info
    self.priority = priority
    
# class for Priority queue 
class PriorityQueue:
  
  def __init__(self):
    self.queue = []
    # if you want you can set a maximum size for the queue
    
  def insert(self, node):
    # if queue is empty
    if self.size() == 0:
      # add the new node
      self.queue.append(node)
    else:
      for index, current in enumerate(self.queue):
          if current.priority < node.priority:
              if index == self.size() - 1:
                  self.queue.insert(index+1, node)
              else:
                  continue
          else:
              self.queue.insert(index, node)
              return True
  
  def delete(self):
    # remove the first node from the queue
    return self.queue.pop(0)
    
  def show(self):
    for x in self.queue:
      print( str(x.info)+" - "+str(x.priority))
  
  def size(self):
    return len(self.queue)
