
Map = [[34, 21, 32, 41, 25],
       [14, 42, 43, 14, 31],
       [54, 45, 52, 42, 23],
       [33, 15, 51, 31, 35],
       [21, 52, 33, 13, 23]]

result = []


def treasure_hunt(map, clue=None):
    if clue is None:
        cell = map[0][0]
    else:
        cell = clue
    result.append(cell)
    coordinate = list(str(cell))
    coordinate_row = int(coordinate[0]) - 1
    coordinate_column = int(coordinate[1]) - 1
    coordinate_target = map[coordinate_row][coordinate_column]

    if coordinate_target == cell:
        print('Congratulation!')
    else:
        treasure_hunt(map, coordinate_target)
    return result


class TreasureHunt:
    def __init__(self):
        self.result = []
        self.cell = None
        self.coordinate_target = None

    def search_treasure(self, map):
        self.cell = map[0][0]
        self.result.append(self.cell)
        coordinate = list(str(self.cell))
        coordinate_row = int(coordinate[0]) - 1
        coordinate_column = int(coordinate[1]) - 1
        self.coordinate_target = map[coordinate_row][coordinate_column]
        while self.coordinate_target != self.cell:
            self.cell = self.coordinate_target
            self.result.append(self.cell)
            coordinate = list(str(self.cell))
            coordinate_row = int(coordinate[0]) - 1
            coordinate_column = int(coordinate[1]) - 1
            self.coordinate_target = map[coordinate_row][coordinate_column]

        return self.result


th = TreasureHunt()


# implementations one
# print(treasure_hunt(Map))

# implementations two
# print(th.search_treasure(Map))


def test_one():
    assert len(treasure_hunt(Map)) <= 25


def test_two():
    assert len(th.search_treasure(Map)) <= 25


def test_three():
    assert [i in Map for i in treasure_hunt(Map)]


def test_foure():
    assert [i in Map for i in th.search_treasure(Map)]


def test_five():
    treasure = treasure_hunt(Map)[-1]
    coordinate = list(str(treasure))
    coordinate_row = int(coordinate[0]) - 1
    coordinate_column = int(coordinate[1]) - 1
    assert treasure == Map[coordinate_row][coordinate_column]


def test_six():
    treasure = th.search_treasure(Map)[-1]
    coordinate = list(str(treasure))
    coordinate_row = int(coordinate[0]) - 1
    coordinate_column = int(coordinate[1]) - 1
    assert treasure == Map[coordinate_row][coordinate_column]
