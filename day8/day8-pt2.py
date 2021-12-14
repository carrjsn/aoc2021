def main():

  with open('day8/day8.txt', 'r') as file:
    lines = file.readlines()

  four_digit_codes = []
  for line in lines:
    section = line.replace('\n', '').split(' | ')
    signals = section[0].split(' ')
    code = section[1].split(' ')


    segments = {}
    # decoding the input
    for alpha in signals:
      # get 1, 4, 7, 8
      if len(alpha) == 2:
        segments[1] = alpha
      elif len(alpha) == 3:
        segments[7] = alpha
      elif len(alpha) == 4:
        segments[4] = alpha
      elif len(alpha) == 7:
        segments[8] = alpha

    # iterate again -  get 0, 9, 6
    for alpha in signals:
      # if len 6
      if len(alpha) == 6:
        # if segments 4, 7 all exist in curr alpha - curr alpha is 9
        if all([ch in alpha for ch in segments[4]]) and all([ch in alpha for ch in segments[7]]):
          segments[9] = alpha

        # if segments 1 doesnt exist in curr alpha - alpha is 6
        elif not all([ch in alpha for ch in segments[1]]):
          segments[6] = alpha
        # if segments 1, 7, exist in curr alpha but not 4 - curr alpha is 0
        elif all([ch in alpha for ch in segments[1]]) and all([ch in alpha for ch in segments[7]]) and not all([ch in alpha for ch in segments[4]]):
          segments[0] = alpha

    # iterate once more and get 3, 5
    for alpha in signals:
      # if len 5
      if len(alpha) == 5:
        # if segments 1 is in curr alpha - curr alpha is 3
        if all([ch in alpha for ch in segments[1]]):
          segments[3] = alpha
        # if curr alpha is in segments 9 - curr alpha is 5
        elif all([ch in segments[9] for ch in alpha]):
          segments[5] = alpha

    # then whichever alpha is not a value in segments dict - that alpha is segments[2]
    segments[2] = list(filter(lambda a : a not in segments.values(), signals))[0]

    # print(segments)

    # # now - decode the four digit code
    string_code = ''
    for dig in code:
      # find value in segments, return key
      for key, val in segments.items():
        if ''.join(sorted(val)) == ''.join(sorted(dig)):
          string_code += str(key)
    four_digit_codes.append(int(string_code))


  print(sum(four_digit_codes))


if __name__ == '__main__':
  main()