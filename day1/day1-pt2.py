
def main():

  with open('day1/day1.txt', 'r') as file:
    lines = file.readlines()

  nums = list(map(lambda l : int(l.replace('\n', '')), lines))

  increasing = 0
  prev_sum = sum(nums[:3])

  for i in range(1, len(nums)):
    currSum = sum(nums[i:i+3])
    if currSum > prev_sum:
      increasing += 1
    prev_sum = currSum

  print(increasing)


if __name__ == '__main__':
  main()