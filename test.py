import unittest
import course as co

def is_finish(cells):
  """ Agent の is_finish と同じ

  向こうは引数として自由に cells を取れないのでここで新しく定義する。
  """

  return any(cell.is_finish() for cell in cells)

class TestIsFinish(unittest.TestCase):
  """ 終了条件の判定が煩雑なのでテストしておく
  """

  def setUp(self):
    cg = co.CourseGenerator()
    self.course = cg.simple_course2()

  def test_not_finish_in_course_1(self):
    a = [10,10]
    b = [15,20]

    cells = self.course.get_cells_betwenn_two_position(a,b)
    result = is_finish(cells)

    self.assertEqual(result, False)
  
  def test_not_finish_in_course_2(self):
    a = [10,10]
    b = [10,20]

    cells = self.course.get_cells_betwenn_two_position(a,b)
    result = is_finish(cells)

    self.assertEqual(result, False)
  
  def test_not_finish_in_course_3(self):
    a = [10,10]
    b = [15,10]

    cells = self.course.get_cells_betwenn_two_position(a,b)
    result = is_finish(cells)

    self.assertEqual(result, False)
  
  def test_not_finish_out_course_1(self):
    a = [20,20]
    b = [40,25]

    cells = self.course.get_cells_betwenn_two_position(a,b)
    result = is_finish(cells)

    self.assertEqual(result, False)

  def test_not_finish_out_course_2(self):
    a = [20,20]
    b = [40,20]

    cells = self.course.get_cells_betwenn_two_position(a,b)
    result = is_finish(cells)

    self.assertEqual(result, False)
  
  def test_finish_on_endcell_1(self):
    a = [25,25]
    b = [25,29]

    cells = self.course.get_cells_betwenn_two_position(a,b)
    result = is_finish(cells)

    self.assertEqual(result, True)

  def test_finish_on_endcell_2(self):
    a = [25,25]
    b = [27,29]

    cells = self.course.get_cells_betwenn_two_position(a,b)
    result = is_finish(cells)

    self.assertEqual(result, True)

  def test_finish_over_endcell_1(self):
    a = [10,27]
    b = [20,40]

    cells = self.course.get_cells_betwenn_two_position(a,b)
    result = is_finish(cells)

    self.assertEqual(result, True)

  def test_finish_over_endcell_2(self):
    a = [10,27]
    b = [10,40]

    cells = self.course.get_cells_betwenn_two_position(a,b)
    result = is_finish(cells)

    self.assertEqual(result, True)

  def test_finish_over_endcell_3(self):
    """ 右に行けるだけ移動してその後下にいく方針を期待するならFalseになるべき
    """

    a = [10,27]
    b = [40,40]

    cells = self.course.get_cells_betwenn_two_position(a,b)
    result = is_finish(cells)

    self.assertEqual(result, False) # False であることに注意



if __name__ == "__main__":
  unittest.main()