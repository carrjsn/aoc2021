def main():

  with open('day2/day2.txt', 'r') as file:
    lines = file.readlines()

  moves = list(map(lambda l : l.replace('\n', ''), lines))

  dirs = {
    'forward': 0,
    'up': 0,
    'down': 0
  }

  for move in moves:
    tup = move.split(' ')
    if tup[0] == 'up':
      dirs['up'] -= int(tup[1])
    else:
      dirs[tup[0]] += int(tup[1])

  depth = dirs['down'] + dirs['up']
  final_position = dirs['forward'] * depth


  print('dirs', dirs)
  print('depth', depth)
  print('final', final_position)


if __name__ == '__main__':
  main()