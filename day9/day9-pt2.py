def main():
  with open('day9/day9.txt') as file:
    files = list(map(lambda line : line.replace('\n', ''), file.readlines()))

  board = [
    ['9', '9', '9'],
    ['9', '9', '9'],
    ['9', '9', '9']
  ]
  basins = []

  # working
  while not board_fully_searched(board):
    print('in board')
    basins.append('hey')

  print(basins)


def gather_basin(matrix, x, y):
  pass

def board_fully_searched(matrix):
  for row in matrix:
    if not all(map(lambda el : el == '9', row)):
      return False
  return True


if __name__ == '__main__':
  main()