def main():
  with open('day12/day12example.txt') as file:
    connections = list(map(lambda line : line.replace('\n', ''), file.readlines()))
  # print(connections)

  # like a graph -- track edges of each node
  # make dict
  edges = {}

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

  # helper function - define up here inside main for closure access to edges dictionary
  def find_valid_paths(path, ele):
    print(path)
    path_count = 0

    # base case
    if ele == 'end':
      path_count += 1
      print('success', path)
      return path_count
    # elif len(edges[ele]) == 1 and edges[ele][0] in path and edges[ele][0].islower():
    #   return 0

    # itereate over arr of edges
    for edge in edges[ele]:
      # don't include 'start' again -
      # dont include any lower case places that have already been visited - in path..
      if (edge.islower() and edge in path) or edge == 'start':
        continue
      else:
        # add the current edge to the path
        path.append(edge)
        path_count += find_valid_paths(path, edge)

    return path_count



  valid_paths = 0

  # iterate over edges[start] and look for valid paths to end
  for edge in edges['start']:
    # find number of valid paths to end for each element

    path = ['start', edge]
    valid_paths += find_valid_paths(path, edge)

  print('valid paths', valid_paths)





if __name__ == '__main__':
  main()