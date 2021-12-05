def main():

  with open('day3example.txt', 'r') as file:
    lines = file.readlines()

  counts = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
  }

  print(lines)
  # get counts for each char in binary nums
  for i in range(len(lines)):
    # each binary num
    for j in range(5):
    # each char in binary num
      if lines[i][j] == '1':
        counts[j] += 1
      else:
        counts[j] -= 1
  # if num is positive, 1 is the more common char
  # if num is negative, 0 is more common char
  print(counts)







if __name__ == '__main__':
  main()


  # try 2 --- misunderstanding
  # oxygen_match = ''
  # scrubber_match = ''
  # # create oxygen / scrubber match based on counts values for filtering out
  # for val in counts.values():
  #   if val >= 0:
  #     oxygen_match += '1'
  #     scrubber_match += '0'
  #   else:
  #     oxygen_match += '0'
  #     scrubber_match += '1'

  # print('match', oxygen_match)

  # ox_answer = ''
  # i = 1
  # while True:
  #   oxy_matches = list(filter(lambda line : line[:i] == oxygen_match[:i], lines))
  #   print(oxy_matches)
  #   if len(oxy_matches) == 1:
  #     # print(oxy_matches[0][:i])
  #     ox_answer = oxy_matches[0]
  #     break
  #   i += 1


  # # j = 8
  # # print(scrubber_match)
  # # scrub_matches = list(filter(lambda line : line[:j] == scrubber_match[:j], lines))
  # # print('sm', scrub_matches)

  # scrub_answer = ''
  # j = 1
  # while True:
  #   scrub_matches = list(filter(lambda line : line[:j] == scrubber_match[:j], lines))
  #   if len(scrub_matches) == 2:
  #     # print(scrub_matches[0][:j])
  #     scrub_answer = scrub_matches[1]
  #     break
  #   j += 1

  # print(ox_answer)
  # print(scrub_answer)
  # print(int(ox_answer, 2) * int(scrub_answer, 2))

  # print(int(oxygen_match, 2))
  # print(int(scrubber_match, 2))
  # print(int(oxygen_match, 2) * int(scrubber_match, 2))



  #try 1 --- wrong
  # oxygen = list(filter(lambda line : bool(int(line[0])) == bool(counts[0]), lines))
  # scrubber = list(filter(lambda line : int(line[0]) and (counts[0]), lines))
  # oxygen = []
  # scrubber = []

  # for line in lines:
  #   if (line[0] == '1' and counts[0] > 0) or (line[0] == '0' and counts[0] <= 0):
  #     oxygen.append(line)
  #   else:
  #     scrubber.append(line)

  # # check that for 0 index, oxygen should be all strings beginning with 1
  # # scrubber should be all strings beginning with 0
  # # print('oxygen', oxygen)
  # # print('scrubber', scrubber)

  # # start at first index since 0 already checked
  # i = 1
  # while len(oxygen) > 1 and len(scrubber) > 1:

  #   new_oxy = list(filter(lambda line : (line[i] == '1' and counts[i] > 0) or (line[i] == '0' and counts[i] <= 0), oxygen))
  #   new_scrub = list(filter(lambda line : (line[i] == '1' and counts[i] <= 0) or (line[i] == '0' and counts[i] > 0), scrubber))
  #   if len(oxygen) > 1:
  #     oxygen = new_oxy
  #   if len(scrubber) > 1:
  #     scrubber = new_scrub
  #   i += 1

  # print('oxygen: ', oxygen)
  # print('scrubber: ', scrubber)

  # idx = 1
  # while len(scrubber) > 1:
  #   new_scrub = list(filter(lambda l : int(l[idx]) <= 0 and counts[idx] <= 0, scrubber))
  #   scrubber = new_scrub
  #   idx += 1

  # print(oxygen)
  # print(scrubber)