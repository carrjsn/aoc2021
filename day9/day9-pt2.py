def main():
  with open('day9/day9.txt') as file:
    files = list(map(lambda line : line.replace('\n', ''), file.readlines()))

  board = list(map(lambda row : list(row), files))
  basins = []

  # working
  # itereate over board rows
  for i in range(len(board)):
    # itereate over columns in row
    for j in range(len(board[i])):
      # check curr ele to see if NOT a string 9
      if board[i][j] != '9':
       # if not a 9 - gather the basin and add (maybe just basin length) to basins
       basins.append(len(gather_basin(board, i, j)))
       # gather_basin should alter the board array changing seen eles to 9s so that they aren't counted again

  # get 3 largest basins and multiply together
  largest_basins = sorted(basins)[-3:]
  print(largest_basins[0] * largest_basins[1] * largest_basins[2])


def gather_basin(matrix, x, y):
  # curr basin arr - (maybe with current coords element already added in?)
  # add current ele to curr basin array if valid? here?
  curr_basin = [matrix[x][y]]

  # if matrix at x, y is a 9 - the current path is not valid - return nothing - kill the current callstack - or make this check before recursing...

  # CHANGE ANY ELEMENTS ADDED TO CURR BASIN ARR to 9s so that they're already seen and not counted twice
  matrix[x][y] = '9'

  # backtrack/recurse - looking above, below, left, right for a valid next step ---------------
  # adding any further collected eles to the curr basin arr

  # check right - make sure next step not out of range
  if y != len(matrix[x]) - 1:
    if matrix[x][y + 1] != '9':
      curr_basin += gather_basin(matrix, x, y + 1)
  # check left
  if y > 0:
    if matrix[x][y - 1] != '9':
      curr_basin += gather_basin(matrix, x, y - 1)
  # check top
  if x > 0:
    if matrix[x - 1][y] != '9':
      curr_basin += gather_basin(matrix, x - 1, y)
  # check bottom
  if x != len(matrix) - 1:
    if matrix[x + 1][y] != '9':
      curr_basin += gather_basin(matrix, x + 1, y)

  #return the curr basin arr
  return curr_basin



if __name__ == '__main__':
  main()



# while not board_fully_searched(board):
#     # itereate over board rows
#       # itereate over columns in row
#         # check curr ele to see if NOT a 9
#           # if not a 9 - gather the basin and add (maybe just basin length) to basins
#           # gather_basin should alter the board array changing seen eles to 9s so that they aren't counted again

#     pass