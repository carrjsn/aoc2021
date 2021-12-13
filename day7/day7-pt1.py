def main():

  with open('day7/day7.txt', 'r') as file:
    lines = file.readlines()
  nums = list(map(int, lines[0].split(',')))

  print(nums)

  least_fuel = float('inf')

  for i in range(len(nums)):
    curr_crab = nums[i]
    curr_fuel = 0
    # compare distance from all other crabs
    for j in range(len(nums)):
      temp_crab = nums[j]
      curr_fuel += abs(curr_crab - temp_crab)
    if curr_fuel < least_fuel:
      least_fuel = curr_fuel

  print(least_fuel)

if __name__ == '__main__':
  main()