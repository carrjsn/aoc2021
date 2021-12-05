def main():

  with open('day5/day5.txt', 'r') as file:
    lines = file.readlines()

  coords = []
  for line in lines:
    curr = line.replace('\n', '')
    coords.append(curr.split(' -> '))

  # make board (matrix)
  board = [[0 for x in range(1000)] for y in range(1000)]

  # itereate over coords
  for coord in coords:
    start = list(map(int, coord[0].split(',')))
    end = list(map(int, coord[1].split(',')))

    # check if horizontal or vertial line
    if start[0] == end[0]:
      # determine what x, y locations get filled in
      # increment all those positions by 1
      for y in range( min(start[1], end[1]), max(start[1], end[1]) + 1 ):
        board[start[0]][y] += 1

    if start[1] == end[1]:
      # determine what x, y locations get filled in
      # increment all those positions by 1
      for x in range( min(start[0], end[0]), max(start[0], end[0]) + 1 ):
        board[x][start[1]] += 1

  # then count how many spaces are greater than 1
  count = 0
  for row in board:
    for el in row:
      if el > 1:
        count += 1

  print('solution', count)


if __name__ == '__main__':
  main()