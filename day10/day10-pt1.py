def main():

  with open('day10/day10.txt') as file:
    files = list(map(lambda line : line.replace('\n', ''), file.readlines()))

    char_vals = {
      ')': 3,
      ']': 57,
      '}': 1197,
      '>': 25137
    }

    char_matches = {
      ')': '(',
      ']': '[',
      '}': '{',
      '>': '<'
    }

    illegals = []

    recent_openings = []
    # itereate over input one row/line at a time
    # detect corrupted lines - break if found and add the illegal char to illegals
    for line in files:
      for char in line:
        # check if curr char is an opening
        if char in '({[<':
          # if so add the recent_openings
          recent_openings.append(char)
        # if curr_char is a closing
        elif char in ')}]>':
          # make sure it matches the last index of recent_openings
          if not len(recent_openings) or recent_openings[-1] != char_matches[char]:
            # if it does not - the line is corrupted - add the illegal char to illegals
            illegals.append(char)
            break
          # if vaild match remove most recent so that next in line is expected
          else:
            recent_openings.pop()


    print(sum(map(lambda ch : char_vals[ch], illegals)))








if __name__ == '__main__':
  main()