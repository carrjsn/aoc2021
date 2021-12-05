def main():

  with open('day3/day3.txt', 'r') as file:
    lines = file.readlines()

  counts = get_bit_counts(lines)

  print('counts', counts)


  # get oxygen num -----------------------------------------------------------------
  oxy_matches = []
  for line in lines:
      if (line[0] == '1' and counts[0] >= 0) or (line[0] == '0' and counts[0] < 0):
        oxy_matches.append(line)

  # iterate
  i = 1
  while True:
    curr_counts = get_bit_counts(oxy_matches)
    # filter remaining matches by whether current bit is a match
    oxy_matches = get_oxy_matches(oxy_matches, curr_counts, i)
    # check for terminal case
    if len(oxy_matches) == 1:
      break
    # increment i
    i += 1


  # get co2 num -----------------------------------------------------------------------
  co2_matches = []
  for line in lines:
      if (line[0] == '1' and counts[0] < 0) or (line[0] == '0' and counts[0] >= 0):
        co2_matches.append(line)

  # iterate
  j = 1
  while True:
    curr_counts = get_bit_counts(co2_matches)
    # filter remaining matches by whether current bit is a match
    co2_matches = get_co2_matches(co2_matches, curr_counts, j)
    # check for terminal case
    if len(co2_matches) == 1:
      break
    # increment i
    j += 1

  oxygen_generator = int(oxy_matches[0], 2)
  co2_scrubber = int(co2_matches[0], 2)

  print('oxy', oxygen_generator)
  print('co2', co2_scrubber)
  print('solution', oxygen_generator * co2_scrubber)


def get_co2_matches(lines, counts, idx):
  matches = []
  for line in lines:
      if (line[idx] == '1' and counts[idx] < 0) or (line[idx] == '0' and counts[idx] >= 0):
        matches.append(line)
  return matches


def get_oxy_matches(lines, counts, idx):
  matches = []
  for line in lines:
      if (line[idx] == '1' and counts[idx] >= 0) or (line[idx] == '0' and counts[idx] < 0):
        matches.append(line)
  return matches


def get_bit_counts(lines):
  counts = {}
  # get counts for each char in binary nums
  for i in range(len(lines)):
    # each binary num
    for j in range(len(lines[0]) - 1):
    # each char in binary num
      if j not in counts.keys():
        counts[j] = 0
      if lines[i][j] == '1':
        counts[j] += 1
      else:
        counts[j] -= 1
  # if num is positive, 1 is the more common char
  # if num is negative, 0 is more common char
  return counts


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