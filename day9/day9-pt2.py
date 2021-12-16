def main():
  with open('day9/day9.txt') as file:
    files = list(map(lambda line : line.replace('\n', ''), file.readlines()))

  board = files[:]
  basins = []

  # working
  while not board_fully_searched(board):
    # itereate over board rows
      # itereate over columns in row
        # check curr ele to see if NOT a 9
          # if not a 9 - gather the basin and add to basins
          # gather_basin should alter the board array changing seen eles to 9s so that they aren't counted again


    pass



  # get 3 largest basins and multiply together
  print(basins)


def gather_basin(matrix, x, y):
  # if matrix at x, y is a 9 - the current path is not valid - return nothing - kill the current callstack

  # CHANGE ANY ELEMENTS ADDED TO CURR BASIN ARR to 9s so that they're already seen and not counted twice

  # curr basin arr - (maybe with current coords element already added in?)
  # start search at x, y coords in matrix
    # add current ele to curr basin array if valid? here?
    # backtrack/recurse - looking above, below, left, right for a valid next step
      # adding any further collected eles to the curr basin arr

  #return the curr basin arr

  pass


def board_fully_searched(matrix):
  for row in matrix:
    if not all(map(lambda el : el == '9', row)):
      return False
  return True


if __name__ == '__main__':
  main()