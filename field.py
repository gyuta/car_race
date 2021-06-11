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

    course = []

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
      course.append(row)

    return course