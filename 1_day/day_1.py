from copy import deepcopy

with open('data.txt') as data_file:
  data = [int(line.replace('\n', '')) for line in data_file]


data.sort()

small_first = deepcopy(data)

data.sort(reverse=True)

big_first = data

for number in big_first:

  for small_number in small_first:
    remainder = 2020 - number - small_number
    if remainder < 0:
      break

    if remainder in data:
      print(small_number, remainder, number)
      print(small_number*remainder*number)





