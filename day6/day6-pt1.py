def main():

  with open('day6/day6.txt', 'r') as file:
    lines = file.readlines()

  fish = list(map(int, lines[0].split(',')))
  print(fish)

  for i in range(80):
    new_fish_count = 0
    for j in range(len(fish)):
      if fish[j] == 0:
        fish[j] = 6
        new_fish_count += 1
      else:
        fish[j] -= 1
    for i in range(new_fish_count):
      fish.append(8)

  print('after 256', len(fish))







if __name__ == '__main__':
  main()