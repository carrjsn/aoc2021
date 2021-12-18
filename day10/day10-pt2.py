import math

def main():

  with open('day10/day10.txt') as file:
    files = list(map(lambda line : line.replace('\n', ''), file.readlines()))

    char_vals = {
      ')': 1,
      ']': 2,
      '}': 3,
      '>': 4
    }

    char_matches = {
      ')': '(',
      ']': '[',
      '}': '{',
      '>': '<',
      '(': ')',
      '[': ']',
      '{': '}',
      '<': '>'
    }


    completion_strings = []
    # itereate over input one row/line at a time
    # detect corrupted lines - break if found and add the illegal char to illegals
    for line in files:
      recent_openings = []
      line_corrupted = False
      for char in line:
        # check if curr char is an opening
        if char in '({[<':
          # if so add the recent_openings
          recent_openings.append(char)
        # if curr_char is a closing
        elif char in ')}]>':
          # make sure it matches the last index of recent_openings
          if not len(recent_openings) or recent_openings[-1] != char_matches[char]:
            # if it does not - the line is corrupted - break out of loop and move onto next line
            line_corrupted = True
            break
          # if vaild match remove most recent so that next in line is expected
          else:
            recent_openings.pop()

      # if no illegals found - it is a incomplete
      if not line_corrupted:
        # create the completion string that makes a valid line
        curr_completion_str = ''
        for ch in recent_openings[::-1]:
          curr_completion_str += char_matches[ch]
        # add to global list
        completion_strings.append(curr_completion_str)


    print(completion_strings)

    scores = []
    for item in completion_strings:
      score = 0
      for ch in item:
        score = score * 5 + char_vals[ch]
      scores.append(score)

    mid_idx = math.floor(len(scores) / 2)
    print(sorted(scores)[mid_idx])


if __name__ == '__main__':
  main()