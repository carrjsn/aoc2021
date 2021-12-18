def main():
  with open ('day11/day11.txt') as file:
    files = list(map(lambda line : list(map(int, list(line.replace('\n', '')))), file.readlines()))
  print(files)

  board = files.copy()

  flashes = 0

  # 100 steps
  for i in range(100):
    # coords that have flashed this step array - so that no octopus flashes more than once per step
    # append as string 'x-y' with dash in-between for easy comparison
    flashes_this_step = []
    # iterate over matrix and increase each octopus by 1
    for x in range(10):
        for y in range(10):
          board[x][y] += 1

    # continue to execute flashes on any nums greater than num - so long as they haven't already flashed
    while flashes_present:
      for x in range(10):
        for y in range(10):
          # if num > 9
            # invoke flash - incrementing all nums around it - add to count
            # change val to 0

      # after iteration - reset any 'flashed' to zero

  print(flashes)


def flash(matrix, x, y):
  # # # SHOULD mutate matrix input
  # increase all surrounding elements by 1
  pass

def flashes_present(matrix):
  # itereate and check board for any eles greater than 9
  pass

if __name__ == '__main__':
  main()