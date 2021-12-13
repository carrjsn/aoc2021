def main():

  with open('day6/day6.txt', 'r') as file:
    lines = file.readlines()

  data = {}
  # list of strings
  fish = list(map(int, lines[0].split(',')))

  for val in range(max(9, max(fish))):
    data[val] = 0
  for ele in fish:
    data[ele] += 1

  for _ in range(256):
    zero_count = data[0]
    # reset zero key
    data[0] = 0
    for idx in range(1, len(data)):
      data[idx - 1] += data[idx]
      data[idx] = 0
    data[6] += zero_count
    data[8] += zero_count

  total_fish = 0
  for key in data:
    total_fish += data[key]

  print(total_fish)


if __name__ == '__main__':
  main()



# TRY 4 - spawn count
# start with the number of input fish - they count too
#   fish_count = len(fish)
#   timespan = 150

#   for i in range(len(fish)):
#     # determine how many lantern fish the current number will create in a given time span?  # add to fish count
#     fish_count += spawn_count(fish[i], timespan)

#   print(fish_count)


# def spawn_count(num, days):
#   # start count at one b/c num is definitely less than day count
#   count = 0
#   births = []

#   # if num = 3, 4 days must go by for a new fish to be born
#   # if num = 3, 11 days must go by for 2 fish to be born

#   # maybe can lose top level if statement b/c if num is greater than days this loop wont run
#   for i in range(num, days, 7):
#     count += 1
#     # add current day for subtracting from TOTAL days when recursing to get an accurate count
#     births.append(i + 1)

#   # now for recursing
#   for day in births:
#     count += spawn_count(8, days - day)

#   # maybe can lose top level if statement
#   return count




  # TRY 2, 3?
  # for incrementing by 7
  # num_map = {
  #   '0': '2',
  #   '1': '3',
  #   '2': '4',
  #   '3': '5',
  #   '4': '6',
  #   '5': '7',
  #   '6': '8',
  #   '7': '0',
  #   '8': '1'
  # }

  # days = 256
  # skip, leftover = divmod(days, 7)


  # # string_fish =
  # # ints for tracking how many new fish a 'chunk' makes every 7 days
  # # regens = []
  # # string fish '34312'
  # for _ in range(skip):

  #   # store sorted fish to represent the potentially new spawned fish (aka --  all fish with timers at 6 or less)
  #   sorted_fish = sorted(fish.copy())

  #   # maybe dont need zero count?
  #   # zero_count = fish.count('0')

  #   # THIS is for generating new chunk to be concatted
  #   new_fish = []

  #   for i in range(len(sorted_fish)):
  #     # ignore 7s and 8s because they won't spawn in 7 days
  #     if int(sorted_fish[i]) < 7:
  #       new_fish.append(num_map[sorted_fish[i]])
  #     else:
  #       # replace 7s with 0s and 8s with 1s on ORIGNAL fish list (first chunk) - leave all other numbers the same??
  #       # not sure if this works here...
  #       fish[i] = num_map[fish[i]]

  #   # replace 7s with 0s and 8s with 1s on ORIGNAL fish list (first chunk) - leave all other numbers the same

  #   # fish = concat old fish + sorted_fish
  #   fish = fish + new_fish

  #   # print('fish', ''.join(fish))


  # # NOW figure out how far away from the target days you are
  # # test - example 4 away from 18

  # extra_fish = list(filter(lambda n : int(n) < leftover, fish))

  # print('after', len(fish) + len(extra_fish))

  # -------------------------------------------------------------------------------------------------------------------



  # string_fish = ''.join(list(lines[0].split(',')))
  # # print(fish)

  # # for incrementing by 7
  # # num_map = {
  # #   0: '2',
  # #   1: '3',
  # #   2: '4',
  # #   3: '5',
  # #   4: '6',
  # #   5: '7',
  # #   6: '8',
  # #   7: '0',
  # #   8: '1'
  # # }

  # # for incrementing one at a time
  # num_map = {
  #   '0': '6',
  #   '1': '0',
  #   '2': '1',
  #   '3': '2',
  #   '4': '3',
  #   '5': '4',
  #   '6': '5',
  #   '7': '6',
  #   '8': '7',
  # }

  # # string_fish =
  # # ints for tracking how many new fish a 'chunk' makes every 7 days
  # # regens = []
  # # string fish '34312'
  # for _ in range(256):
  #   # store curr fish arr

  #   zero_count = string_fish.count('0')

  #   # set to 7 so that it's actually correctly set to 6 after iteration below
  #   string_fish = string_fish.replace('0', '7')

  #   for key, val in num_map.items():
  #     string_fish = string_fish.replace(key, val)

  #   string_fish += '8' * zero_count

  #   # sort fish nums
  #   # fish_sort = ''.join(sorted(list(curr_fish)))
  #   # make new arr for adding on to original