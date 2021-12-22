def main():
  with open('day12/day12example.txt') as file:
    connections = list(map(lambda line : line.replace('\n', ''), file.readlines()))
  # print(connections)

  # like a graph -- track edges of each node
  # make dict
  edges = { }

  for connection in connections:
    first, second = connection.split('-')
    if first not in edges:
      edges[first] = [second]
    else:
      edges[first].append(second)
    if second not in edges:
      edges[second] = [first]
    else:
      edges[second].append(first)

  for key in edges:
    print(key, edges[key])








if __name__ == '__main__':
  main()