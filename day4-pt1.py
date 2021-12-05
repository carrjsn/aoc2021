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

      # if winning board found, do the winning stuff here
        # sum of all unmarked numbers (aka string nums) on the winning board
        # multiply by the curr_num that resulted in win



def check_winning_row(matrix):
  # check if any rows are all ints
  pass

def check_winning_col(matrix):
  # check if any columns are all ints
  pass

if __name__ == '__main__':
  main()