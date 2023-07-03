import time


def find_internal_nodes_num(tree):
  start = time.time()
  #create the empty  set
  parent_nodes = set()
  #going through loop 
  for node in L:
      if node != -1:
          parent_nodes.add(node)
  end = time.time()
  dif =end- start
  return len(parent_nodes)

L = [4, 4, 1, 5, -1, 4, 5]
print(find_internal_node_num(L))


def find_internal_nodes_num(tree):
    start = time.time()
    #Convert the list into set
    parent_nodes = set(L)
    #-1 is removed because its root node(doesnt have parent)
    parent_nodes.remove(-1)  
    end = time.time()
    dif =end- start
    return len(parent_nodes)

L = [4, 4, 1, 5, -1, 4, 5]
print(find_internal_nodes_num(L))  

