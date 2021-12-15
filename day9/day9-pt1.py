def main():
  with open('day9/day9.txt') as file:
    files = list(map(lambda line : line.replace('\n', ''), file.readlines()))

  low_points = []
  for i in range(len(files)):
    for j in range(len(files)):
      curr = int(files[i][j])

      top = float('inf') if i <= 0 else files[i - 1][j]
      bottom = float('inf') if i == len(files) - 1 else files[i + 1][j]
      left = float('inf') if j == 0 else files[i][j - 1]
      right = float('inf') if j == len(files) - 1 else files[i][j + 1]

      if all(map(lambda pos : pos > curr, [top, bottom, left, right])):
        low_points.append(curr)








      # # if all squares north, south, east, west are all higher OR undefined than curr square - add to low_points
      # # -----------------
      # if i == 0:
      #   # no top, no left
      #   if j == 0:
      #     if int(files[i + 1][j]) > curr and int(files[i][j + 1]) > curr:
      #       low_points.append(curr)
      #   # no top
      #   else:
      #     if int(files[i + 1][j]) > curr and int(files[i][j + 1]) > curr and int(files[i][j - 1]) > curr:
      #       low_points.append(curr)


      # # no bottom, no right
      # elif i == len(files) - 1:
      #   if j == len(files) - 1:
      #     if files[i - 1][j] > curr and files[i][j - 1] > curr:
      #       low_points.append(curr)
      #   # no bottom
      #   else:
      #     if files[i - 1][j] > curr and files[i][j + 1] > curr and files[i][j - 1] > curr:
      #       low_points.append(curr)

      # # no top, no right
      # elif j == len(files) - 1:
      #   if i == 0:
      #     if files[i + 1][j] > curr and files[i][j - 1] > curr:
      #       low_points.append(curr)
      #   # no right
      #   else:
      #     if files[i][j] > curr and files[i][j + 1] > curr and files[i][j - 1] > curr:
      #       low_points.append(curr)


      # # no bottom, no left
      # elif j == 0:
      #   if i == len(files) - 1:
      #     if files[i - 1][j] > curr and files[i][j + 1] > curr:
      #       low_points.append(curr)
      #   # no left
      #   else:
      #     print(len(files))
      #     print(i, j)
      #     # if files[i + 1][j] > curr and files[i][j + 1] > curr and files[i - 1][j] > curr:
      #     #   low_points.append(curr)



  print(low_points)

  print('sum', sum(map(lambda n : int(n) + 1, low_points)))






if __name__ == '__main__':
  main()