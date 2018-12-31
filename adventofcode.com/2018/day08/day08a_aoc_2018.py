input = ""

class Node() :
  def __init__(self, data) :
    n_child = int(data.pop(0))
    n_metadata = int(data.pop(0))
    self.children = [ Node(data) for _ in range(n_child) ]
    self.metadata = [ int(data.pop(0)) for _ in range(n_metadata) ]
        
  def count(self) :
    return sum(self.metadata) + sum( [ child.count() for child in self.children ] )

  def value(self) :            
    return sum(self.metadata) if len(self.children) == 0 else self.childvalue()

  def childvalue(self) :
    return sum( self.children[index-1].value() if index != 0 and index <= len(self.children) else 0 for index in self.metadata )
    
Node(input.split()).count()
