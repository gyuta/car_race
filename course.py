import random
import itertools
import functools

class Cell:
  """ Course を構成する1マス。state に対応。
  """

  # レンダリングされる際の色を表す
  COLOR = 'gray'

  # デバッグ用の表示
  SYMBLE = 'O'

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def tag(self):
    """ レンダリングする時に他のセルと区別するためのタグ
    """

    return f"x={self.x},y={self.y}"
  
  def is_finish(self):
    return False
  
  def is_not_empty(self):
    return True

class StartCell(Cell):
  COLOR = 'red'
  SYMBLE = 'S'

class EndCell(Cell):
  COLOR = 'green'
  SYMBLE = 'E'

  def is_finish(self):
    return True

class EmptyCell(Cell):
  """ コース外を表すセル
  """
  COLOR = "black"
  SYMBLE = 'X'

  def is_not_empty(self):
    return False

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
  
  def curve_course1(self):
    """

    カーブしているコースを作成する
    """

    cells = []
    for y in range(30):
      row = []
      for x in range(30):

        if y < 10:
          if x < 10:
            cell = Cell(x,y) if y != 0 else StartCell(x,y)
          else:
            cell = EmptyCell(x,y)
        elif y > 15:
          if x > 20:
            cell = Cell(x,y) if y != 29 else EndCell(x,y)
          else:
            cell = EmptyCell(x,y)
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

  def get_all_cell_list(self):
    return list(itertools.chain.from_iterable(self.cells))
  
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
      cell = self.get_cell(pos)
      return cell.is_not_empty()
    else:
      return False
  
  def get_random_start_cell(self):
    return random.sample(self.startcell_set, 1)[0]

  def get_cells_betwenn_two_position(self, pos_a, pos_b):
    """ 2つのポジションが与えられた場合に、その間にあるセルをリストで返す。端点を含む。

    探索の順番は、先に右に行ってから下に降りる
    pos_a <= pos_b である必要がある（すべての要素に対して）

    途中でコースアウトする場合はその直前までのセルのリストを返す。

    TODO: なめらかに２つのcellをつなげるようにする
    """

    if not (pos_a[0] <= pos_b[0] and pos_a[1] <= pos_b[1]):
      return []

    x = pos_a[0]
    y = pos_a[1]

    result = []
    while x != pos_b[0]:
      if self.is_on_course([x,y]):
        result.append(self.get_cell([x,y]))
      else:
        break
      x += 1
    
    while y!= pos_b[1]:
      if self.is_on_course([x,y]):
        result.append(self.get_cell([x,y]))
      else:
        break
      y += 1
    
    if self.is_on_course([x,y]):
      result.append(self.get_cell([x,y]))
    
    return result
  
  def print(self):
    """ デバッグ用にコースをターミナルに出力する
    """

    for row in self.cells:
      print(functools.reduce(lambda acc, cur: f"{acc} {cur.SYMBLE}", row, ""))


# テスト用
if __name__ == "__main__":
  cg = CourseGenerator()
  c = cg.curve_course1()
  c.print()

