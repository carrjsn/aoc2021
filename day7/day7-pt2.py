def main():

  with open('day7/day7.txt', 'r') as file:
    lines = file.readlines()
  crab_locs = list(map(int, lines[0].split(',')))

  least_fuel = float('inf')

  for idx in range(min(crab_locs), max(crab_locs)):
    curr_fuel = 0
    # compare distance from all other crabs
    for j in range(len(crab_locs)):
      curr_crab = crab_locs[j]
      curr_fuel += get_fuel_cost(idx, curr_crab)

    if curr_fuel < least_fuel:
      least_fuel = curr_fuel

  print(least_fuel)


def get_fuel_cost(num1, num2):
  cost = 0
  diff = abs(num1 - num2)
  for i in range(diff + 1):
    cost += i
  return cost

if __name__ == '__main__':
  main()