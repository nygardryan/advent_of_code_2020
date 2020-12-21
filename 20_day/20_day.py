import re
import numpy


with open('data.txt') as data_file:
  data = [line for line in data_file]

data_dict = {}








class Tile:
  tile_id = None
  raw_data = None

  def __init__(self, key1, value1):
    self.tile_id = key1
    self.raw_data = numpy.array(value1['raw'])

  def flip_lr(self):
    self.raw_data = numpy.fliplr(self.raw_data)

  def flip_up(self):
    self.raw_data = numpy.flipud(self.raw_data)

  def rotate(self):
    self.raw_data = numpy.rot90(self.raw_data)



  @property
  def top_column(self):
    return [x[0] for x in self.raw_data]

  @property
  def bottom_column(self):
    return [x[-1] for x in self.raw_data]



tiles = []



current_tile = None
for line in data:
  if 'Tile ' in line:
    result = re.search('([\d])\w+', line)
    data_dict[result.group(0)] = {}
    current_tile = result.group(0)
    data_dict[current_tile]['raw'] = []
  else:
    dat = line.replace('\n', '')
    if dat:
      data_dict[current_tile]['raw'].append(list(dat))

# {'2039': {'raw': ['##.###..#.\n', '...#.....#\n', '..#...##.#\n', '##.#.#...#\n', '#....#..#.\n', '#.####...#\n',
# '...##...##\n', '##...##..#\n', '#.....##.#\n', '####.#.#.#\n', '\n']}}

for key, value in data_dict.items():
  tiles.append(Tile(key, value))





