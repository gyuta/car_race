import course
import tkinter
import time

class Viewer:

  def __init__(self, RL, start_drawing = 1000 ,width = 800, height = 800):
    self.RL = RL
    self.start_drawing = start_drawing

    root = tkinter.Tk()
    root.title("car race")
    root.geometry(f"{width}x{height}")

    canvas = tkinter.Canvas(
      root,
      width = width,
      height = height,
    )

    canvas.pack()

    info_window = tkinter.Toplevel(root)

    label = tkinter.Label(info_window, text='information')
    label.pack()
    label_count = tkinter.Label(info_window, text='count: 0')
    label_count.pack()
    label_episode = tkinter.Label(info_window, text='episode: 0')
    label_episode.pack()

    self.label_count = label_count
    self.label_episode = label_episode

    self.root = root
    self.canvas = canvas
    self.info_window = info_window

    self.render_course(RL.agent.course)

    canvas.bind_all('<Return>', self.start)

  def start(self, event):
    """ 計算を開始する

    別のクラスに切り出すべきか
    """

    for ep in range(self.RL.max_episode):

      self.label_episode['text'] = f'episode: {ep + 1}'
      trajectory = self.RL.do_episode()

      if ep >= self.start_drawing:
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

    直近{MAX}個のセルをスロットにいれ、描画する。
    colors は軌跡の色を表現する
    """
    colors = ['#0000ff', '#1414ff', '#2828ff', '#3c3cff', '#5050ff', '#6464ff', '#7878ff', '#8c8cff', '#a0a0ff', '#b4b4ff']

    MAX = 5
    slot = []
    count = 0

    for cell in trajectory:
      count += 1

      slot.insert(0, cell)

      if len(slot) > MAX:
        c = slot.pop(-1)
        self.canvas.itemconfig(c.tag(), fill=c.COLOR)

      for i, c in enumerate(slot):
        # TODO: 一箇所にとどまった場合に色が薄くなってしまうのを修正したい
        self.canvas.itemconfig(c.tag(), fill=colors[i])
      time.sleep(0.1)
      self.label_count['text'] = f'count: {count}'
      self.root.update()
    
    # 軌跡を削除
    for cell in slot:
      self.canvas.itemconfig(cell.tag(), fill=cell.COLOR)


if __name__ == '__main__':
  cg = course.CourseGenerator()
  course = cg.simple_course()

  viewer = Viewer()
  viewer.render_course(course)
  viewer.root.mainloop()