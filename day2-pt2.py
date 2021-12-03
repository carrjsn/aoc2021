def main():

  with open('day2.txt', 'r') as file:
    lines = file.readlines()

  moves = list(map(lambda l : l.replace('\n', ''), lines))

  dirs = {
    'forward': 0,
    'aim': 0,
    'depth': 0
  }

  for move in moves:
    tup = move.split(' ')
    if tup[0] == 'up':
      dirs['aim'] -= int(tup[1])
    elif tup[0] == 'down':
      dirs['aim'] += int(tup[1])
    #
    else:
      dirs['forward'] += int(tup[1])
      dirs['depth'] += dirs['aim'] * int(tup[1])

  final_position = dirs['forward'] * dirs['depth']

  print('dirs', dirs)
  print('depth', dirs['depth'])
  print('final', final_position)

if __name__ == '__main__':
  main()