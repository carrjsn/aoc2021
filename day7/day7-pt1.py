def main():

  with open('day7/day7.txt', 'r') as file:
    lines = file.readlines()
  nums = list(map(int, lines[0].split(',')))

  print(nums)


if __name__ == '__main__':
  main()