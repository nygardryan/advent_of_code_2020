

with open('data.txt') as data_file:
  data = [int(line.replace('\n', '')) for line in data_file]


found_solution = None
for number in data:
  x = 2020 - number
  if x in data:
    print("Solution is: ", x * number)