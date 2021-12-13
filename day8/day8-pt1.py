def main():

  with open('day8/day8.txt', 'r') as file:
    lines = file.readlines()

  count = 0
  for line in lines:
    code = line.split(' | ')[1].replace('\n', '')
    digits = code.split(' ')
    for dig in digits:
      if len(dig) in [2, 3, 4, 7]:
        count += 1

  print(count)


if __name__ == '__main__':
  main()