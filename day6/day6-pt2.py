def main():

  with open('day6/day6.txt', 'r') as file:
    lines = file.readlines()

  fish = list(map(int, lines[0].split(',')))
  print(fish)

  # ints for tracking how many new fish a 'chunk' makes every 7 days
  # regens = []

  for i in range(256):
    zero_count = fish.count(0)
    fish = [n - 1 if n > 0 else 6 for n in fish]
    for i in range(zero_count):
      fish.append(8)

  print('after 80', len(fish))


if __name__ == '__main__':
  main()