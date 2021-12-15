def main():
  with open('day9/day9.txt') as file:
    files = list(map(lambda line : line.replace('\n', ''), file.readlines()))

  low_points = []
  for i in range(len(files)):
    for j in range(len(files)):
      curr = int(files[i][j])

      top = float('inf') if i <= 0 else int(files[i - 1][j])
      bottom = float('inf') if i == len(files) - 1 else int(files[i + 1][j])
      left = float('inf') if j == 0 else int(files[i][j - 1])
      right = float('inf') if j == len(files) - 1 else int(files[i][j + 1])

      if all(map(lambda pos : pos > curr, [top, bottom, left, right])):
        low_points.append(curr)

  print(low_points)

  print('sum', sum(map(lambda n : int(n) + 1, low_points)))






if __name__ == '__main__':
  main()