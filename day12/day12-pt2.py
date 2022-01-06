def main():
  with open('day12/day12example.txt') as file:
    connections = list(map(lambda line : line.replace('\n', ''), file.readlines()))
  # print(connections)

  # like a graph -- track edges of each node
  # make dict
  edges = {}
  small_caves = []

  for connection in connections:
    first, second = connection.split('-')
    if first.islower() and first not in small_caves and first not in ['start', 'end']:
      small_caves.append(first)
    if second.islower() and second not in small_caves and second not in ['start', 'end']:
      small_caves.append(second)

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


  # somehow make a note of all the lower case (small caves) here in a list []
  # then for each path creation designate one of the small caves that will be allowed to be visited twice
  # print('small caves', small_caves)
  # [a, b, d]
  valid_paths_found = []

  # helper function - define up here inside main for closure access to edges dictionary
  def find_valid_paths(path, ele, small_cave_visited_twice, small_cave):
    path_count = 0

    # base case
    if ele == 'end':
      string_path = ''.join(path)
      if string_path not in valid_paths_found:
        valid_paths_found.append(string_path)
        path_count += 1
        print(path)
        return path_count
      else:
        return 0

    # itereate over arr of edges
    for edge in edges[ele]:

      # don't include 'start' again -
      # dont include any lower case places that have already been visited in path - if they are not the designated small cave..
      if (edge.islower() and edge in path and edge != small_cave) or edge == 'start':
        continue
      elif edge.islower() and edge == small_cave and small_cave_visited_twice:
        continue
      else:
        # if current edge is a small cave and is already been traveled to, check if it is the designated small cave that is allowed to be traveled to twice!
        if edge == small_cave and edge in path:
          small_cave_visited_twice = True
        # don't change input path, but make new unique path for recursion - with the current edge appended to it
        new_path = path + [edge]
        path_count += find_valid_paths(new_path, edge, small_cave_visited_twice, small_cave)

    return path_count



  valid_paths = 0

  # iterate over edges[start] and look for valid paths to end
  for edge in edges['start']:

    # itereate again over each small cave so you can specify which one is allowed to be visited twice
    for cave in small_caves:
      # find number of valid paths to end for each element
      path = ['start', edge]
      print(path, cave)
      valid_paths += find_valid_paths(path, edge, False, cave)

  print('valid paths', valid_paths)



if __name__ == '__main__':
  main()