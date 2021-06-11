import course
import tkinter
import time

class Viewer:

  def __init__(self, RL, width = 800, height = 800):
    self.RL = RL

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

    self.render_course(RL.agent.course)

    canvas.bind_all('<Return>', self.start)

  def start(self, event):
    """ 計算を開始する

    別のクラスに切り出すべきか
    """

    for ep in range(self.RL.max_episode):
      trajectory = self.RL.do_episode()
      self.render_trajectory(trajectory)

  def render_course(self, course):
    """ course をレンダリングする
    """
    width = 10
    height = 10
    for i, row in enumerate(course.cells):
      for j, cell in enumerate(row):
        x = j*width
        y = i*height
        self.canvas.create_rectangle(
          x, y, x + width, y + height,
          fill=cell.COLOR,
          tag=cell.tag(),
          outline='white'
        )

  def render_trajectory(self, trajectory):
    """ trajectory(軌跡)をレンダリングする
    """
    # trajectory = ['x=5,y=5','x=5,y=6','x=5,y=7','x=5,y=8','x=6,y=9','x=7,y=9','x=7,y=10']
    for cell in trajectory:
      self.canvas.itemconfig(cell.tag(), fill='blue')
      time.sleep(0.2)
      self.root.update()


if __name__ == '__main__':
  cg = course.CourseGenerator()
  course = cg.simple_course()

  viewer = Viewer()
  viewer.render_course(course)
  viewer.root.mainloop()

  # trajectory = ['x=5,y=5','x=5,y=6','x=5,y=7','x=5,y=8','x=6,y=9','x=7,y=9','x=7,y=10']
  # print('hoge')
  # viewer.render_trajectory(trajectory)