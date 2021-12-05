def main():

  with open('day4.txt', 'r') as file:
    lines = file.readlines()

  # print(lines)
  content = ''.join(lines).split('\n')

  # separate numbers for game input
  nums = content[0].split(',')

  # separate boards
  boards = []
  curr_board = []
  for line in content[2:]:
    if line != '':
      # filter out empty whitespace elements that occur with single digit nums
      curr_row = list(filter(lambda el : el != '', line.split(' ')))
      curr_board.append(curr_row)
    else:
      boards.append(curr_board)
      curr_board = []

  # iterate over nums one at a time
  for num in nums:

    # make current num on each board into a int? or flag it somehow?
    for i in range(len(boards)):
      for row in range(5):
        for col in range(5):
          if boards[i][row][col] == num:
            boards[i][row][col] = int(num)

    # then check if that move results in any boards containing a winning bingo row (i.e. all ints in a row or column)
    for board in boards:
      # if winning board found, do the winning stuff here
      if (check_winning_row(board) or check_winning_col(board)):
        print('winning board', board)
        print('winning num', num)
        # sum of all unmarked numbers (aka string nums) on the winning board
        unmarked_sum = get_sum_of_unmarked_nums(board)
        # multiply by the curr_num that resulted in win
        print('solution', unmarked_sum * int(num))
        raise StopIteration


def get_sum_of_unmarked_nums(matrix):
  unmarked_nums = []
  for row in matrix:
    for el in row:
      if isinstance(el, str):
        unmarked_nums.append(int(el))
  return sum(unmarked_nums)

def check_winning_row(matrix):
  # check if any rows are all ints
  for row in matrix:
    if all([isinstance(x, int) for x in row]):
      return True
  return False

def check_winning_col(matrix):
  # check if any columns are all ints
  for col in range(5):
    curr_col = [ matrix[0][col], matrix[1][col], matrix[2][col], matrix[3][col], matrix[4][col] ]
    if all([isinstance(el, int) for el in curr_col]):
      return True
  return False

if __name__ == '__main__':
  main()