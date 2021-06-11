class Cell:
  # レンダリングされる際の色を表す
  COLOR = 'gray'

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
          cell = StartCell()
        elif y == 59:
          cell = EndCell()
        else:
          cell = Cell()

        row.append(cell)
      course.append(row)

    return course