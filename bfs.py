graph = {
  'A' : [['B','no'],['C', 'no']],
  'B' : [['D','no'],['E', 'no']],
  'C' : [['F','yes'],['G', 'no']],
  'D' : [['H','no']],
  'E' : [['I','no'],['J', 'yes']],
  'F' : [['K','no']],
  'G' : [],
  'H' : [['D','no']],
  'I' : [],
  'J' : [],
  'K' : []
}


visited = [] # List to keep track of visited nodes.
queue = []   #Initialize a queue
path = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
 

  while queue:
    s = queue.pop(0)
    path.append(s)
    for neighbour in graph[s]:
         if neighbour[0] not in visited:
            visited.append(neighbour[0])
            queue.append(neighbour[0])
            path[s].append(s);
            path[s].append(neighbour[0]);
        
        
        
        print (neighbour[0])
        print(" ")
        print (neighbour[1])
        print('\n')

# Driver Code
bfs(visited, graph, 'A')
print('\n')