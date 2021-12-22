def main():
  with open('day12/day12.txt') as file:
    files = list(map(lambda line : line.replace('\n', ''), file.readlines()))
  print(files)





if __name__ == '__main__':
  main()