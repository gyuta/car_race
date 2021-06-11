import field
import tkinter

class Viewer:

  def __init__(self, width = 800, height = 800):
    root = tkinter.Tk()
    root.title("car race")
    root.geometry(f"{width}x{height}")

    canvas = tkinter.Canvas(
      root,
      width = width,
      height = height,
    )

    canvas.pack()

    self.root = root
    self.canvas = canvas

  def render(self, course):
    """ course をレンダリングする
    """
    width = 10
    height = 10
    for i, row in enumerate(course):
      for j, cell in enumerate(row):
        x = j*width
        y = i*height
        self.canvas.create_rectangle(
          x, y, x + width, y + height,
          fill=cell.COLOR,
          outline='white'
        )
    self.root.mainloop()


if __name__ == '__main__':
  cg = field.CourseGenerator()
  course = cg.simple_course()

  viewer = Viewer()
  viewer.render(course)