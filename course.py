import random

class Cell:
  """ Course を構成する1マス。state に対応。
  """

  # レンダリングされる際の色を表す
  COLOR = 'gray'

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def tag(self):
    """ レンダリングする時に他のセルと区別するためのタグ
    """

    return f"x={self.x},y={self.y}"

class StartCell(Cell):
  COLOR = 'red'

class EndCell(Cell):
  COLOR = 'green'

class CourseGenerator:
  def simple_course(self):
    """

    30x60 の基本的なコースを作成する。スタートラインは上端、エンドラインは下端。
    """

    cells = []

    for y in range(60):
      row = []
      for x in range(30):

        if y == 0:
          cell = StartCell(x,y)
        elif y == 59:
          cell = EndCell(x,y)
        else:
          cell = Cell(x,y)

        row.append(cell)
      cells.append(row)

    return Course(cells)

  def simple_course2(self):
    """

    30x30 の基本的なコースを作成する。スタートラインは上端、エンドラインは下端。
    """

    cells = []

    for y in range(30):
      row = []
      for x in range(30):

        if y == 0:
          cell = StartCell(x,y)
        elif y == 29:
          cell = EndCell(x,y)
        else:
          cell = Cell(x,y)

        row.append(cell)
      cells.append(row)

    return Course(cells)

class Course:
  def __init__(self, cells):
    self.cells = cells

    self.startcell_set = self.get_cell_set('StartCell')
    self.endcell_set = self.get_cell_set('EndCell')

  def get_cell_set(self, target_name):
    group = set()
    for row in self.cells:
      for cell in row:
        if cell.__class__.__name__ == target_name:
          group.add(cell)
    return group
  
  def get_cell(self, pos):
    x = pos[0]
    y = pos[1]
    return self.cells[y][x]

  def is_on_course(self, pos):
    """ ポジションがコース上にあるかどうかを判定する
    """
    x = pos[0]
    y = pos[1]

    if not (0 <= y and y < len(self.cells)):
      return False

    row = self.cells[y]

    if 0 <= x and x < len(row):
      return True
    else:
      return False
  
  def get_random_start_cell(self):
    return random.sample(self.startcell_set, 1)[0]
