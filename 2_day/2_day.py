import re

valid_passwords = 0

with open('data.txt') as data_file:
  data = [line.replace('\n', '').split(" ") for line in data_file]



for iterator in range(len(data)):
  regex_groups = re.findall("\d+", data[iterator][0])
  diction = {"min": int(regex_groups[0]), "max": int(regex_groups[1]), "letter": data[iterator][1][0], "password": data[iterator][2]}

  count = 0
  if diction["password"][diction["min"] - 1] == diction["letter"]:
    count += 1

  if diction["password"][diction["max"] - 1] == diction["letter"]:
    count += 1

  if count == 1:
    valid_passwords += 1


print(valid_passwords)


