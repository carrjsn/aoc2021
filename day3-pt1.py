def main():

  with open('day3.txt', 'r') as file:
    lines = file.readlines()

  counts = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
  }

  # get counts for each char in binary nums
  for i in range(len(lines)):
    # each binary num
    for j in range(12):
    # each char in binary num
      if lines[i][j] == '1':
        counts[j] += 1
      else:
        counts[j] -= 1

  print(counts)
  gamma = ''
  epsilon = ''
  # produce gamma/epsilon rates
  for i in range(12):
    if counts[i] > 0:
      gamma += '1'
      epsilon += '0'
    else:
      gamma += '0'
      epsilon += '1'

  # need to convert to decimal
  print(int(gamma), int(epsilon))
  print(int(gamma, 2) * int(epsilon, 2))


if __name__ == '__main__':
  main()