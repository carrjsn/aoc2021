def main():
  with open ('day11/day11.txt') as file:
    files = list(map(lambda line : list(map(int, list(line.replace('\n', '')))), file.readlines()))
  # print(files)

  board = files.copy()

  flashes = 0

  # 100 steps
  for i in range(500):
    # store coords that have flashed this step array - so that no octopus flashes more than once per step
    # append as string 'x-y' with dash in-between for easy comparison
    flashes_this_step = []
    # iterate over matrix and increase each octopus by 1
    for x in range(10):
        for y in range(10):
          board[x][y] += 1

    # continue to execute flashes on any nums greater than num - so long as they haven't already flashed
    while flashes_present(board):
      for x in range(10):
        for y in range(10):
          # if num > 9 and the number has NOT been flashed this round
          str_coords = str(x) + '-' + str(y)
          if board[x][y] > 9 and str_coords not in flashes_this_step:
            # invoke flash - incrementing all nums around it - add to count
            flash(board, x, y)
            # increment global flashes count
            flashes += 1
            # add coords to flashes-this-step arr
            flashes_this_step.append(str_coords)

      # after iteration - reset any 'flashed' els to zero so it doesn't flash again this step/turn
      for coord in flashes_this_step:
        row = int(coord.split('-')[0])
        col = int(coord.split('-')[1])
        board[row][col] = 0

    if len(flashes_this_step) == 100:
      print(i + 1)


def flash(matrix, x, y):
  # # # SHOULD mutate matrix input
  # increase all surrounding elements by 1

  # check right - make sure next step not out of range
  if y != len(matrix[x]) - 1:
    matrix[x][y + 1] += 1
    # check top-right diag
    if x > 0:
      matrix[x - 1][y + 1] += 1
    # check bottom-right
    if x != len(matrix) - 1:
      matrix[x + 1][y + 1] += 1

  # check left
  if y > 0:
    matrix[x][y - 1] += 1
    # check top-left diag
    if x > 0:
      matrix[x - 1][y - 1] += 1
    # check bottom-left
    if x != len(matrix) - 1:
      matrix[x + 1][y - 1] += 1

  # check top
  if x > 0:
    matrix[x - 1][y] += 1
    # check top-left diag

  # check bottom
  if x != len(matrix) - 1:
    matrix[x + 1][y] += 1
  # no return...


def flashes_present(matrix):
  # itereate and check board for any eles greater than 9
  for x in range(10):
    for y in range(10):
      if matrix[x][y] > 9:
        return True
  return False


if __name__ == '__main__':
  main()