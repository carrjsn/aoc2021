# import pandas as pd


def main():

  with open('day1/day1.txt', 'r') as file:
    lines = file.readlines()

  increasing = 0

  for i in range(1, len(lines)):
    if (int(lines[i].replace('\n', '')) > int(lines[i-1].replace('\n', ''))):
      increasing += 1

  print(increasing)


if __name__ == '__main__':
  main()

