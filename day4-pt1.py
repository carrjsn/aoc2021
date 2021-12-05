def main():

  with open('day4.txt', 'r') as file:
    lines = file.readlines()

  # print(lines)
  content = ''.join(lines).split('\n')


  # separate numbers for game input - make into ints?
  # nums = list(map(int, content[0].split(',')))
  nums = content[0].split(',')
  print(nums)

  boards = []
  # separate boards
  curr_board = []
  for line in content[2:]:
    if line != '':
      # filter out empty whitespace elements that occur with single digit nums
      row = list(filter(lambda el : el != '', line.split(' ')))
      curr_board.append(row)
    else:
      boards.append(curr_board)
      curr_board = []

  # print('boards', boards)



if __name__ == '__main__':
  main()