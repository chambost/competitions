input = ""

class Node() :
  def __init__(this, data) :
    this.n_child = int(data.pop(0))
    this.n_metadata = int(data.pop(0))
    this.subnodes = []
    for ii in range(this.n_child) :
        this.subnodes.append( Node( data ) )
    this.metadata = []
    for jj in range(this.n_metadata) :
        this.metadata.append( int(data.pop(0)) )
        
  def count(self) :
    total = sum(self.metadata)
    for child in self.subnodes :
        total += child.count()
    return total

  def childvalue(self) :
    total = 0
    for index in self.metadata :
      if index != 0 and index <= self.n_child :
        total += self.subnodes[index-1].value()
    return total
        
  def value(self) :            
    return sum(self.metadata) if self.n_child == 0 else self.childvalue()
    
Node(input.split()).count()
