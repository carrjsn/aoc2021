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

    x_decreasing = False
    y_decreasing = False
    x_start = start[0]
    x_end = end[0] + 1
    x_step = 1
    y_start = start[1]
    y_end = end[1] + 1
    y_step = 1
    # determine if start x is less than end x
    if start[0] > end[0]:
      # then you want a decrementing inclusive loop for x
      x_decreasing = True
    # determine if start y is less than end y
    if start[1] > end[1]:
      # then you want a decrementing inclusive loop for y
      y_decreasing = True

    if x_decreasing:
      x_start = start[0]
      x_end = end[0] - 1
      x_step = -1

    if y_decreasing:
      y_start = start[1]
      y_end = end[1] - 1
      y_step = -1


    x = x_start
    y = y_start
    while x != x_end or y != y_end:
      if y == y_end:
        y = y_end - y_step
      if x == x_end:
        x = x_end - x_step

      board[y][x] += 1

      if x != x_end:
        x += x_step
      if y != y_end:
        y += y_step


  # then count how many spaces are greater than 1
  count = 0
  for row in board:
    for el in row:
      if el > 1:
        count += 1

  print('solution', count)


if __name__ == '__main__':
  main()