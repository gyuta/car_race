import random
import itertools

class Agent:
  def __init__(self, course):
    self.position = [0,0] #仮
    self.velocity = [0,0]
    self.action_list = list(itertools.product([-1,0,1], [-1,0,1]))
    
    # agent が course に対しての知識を持たないべきか？
    self.course = course

  def go(self):
    """ 1エピソード分行動する
    """

    result = Result()

    while True:
      if self.is_courseout() or self.is_cross_trajectory():
        self.move_to_start()

      print('position', self.position, self.is_courseout())

      if self.is_finish():
        break

      result.record_reward(-1)
      result.record_state(self.get_cell())

      action = self.select_action()
      result.record_action(action)

      self.apply_action(action)
      self.move()
    
    return result

  def learn(self, result):
    pass

  def move(self):
    self.position = [sum(p) for p in zip(self.position, self.velocity)]

  def move_to_start(self):
    cell = self.course.get_random_start_cell()
    self.position = [cell.x, cell.y]
    print('move to start')

  def select_action(self):
    # ランダムポリシーに対応するやつ。仮置き
    action = random.choice(self.action_list)

    return action

  def apply_action(self, action):
    self.velocity = [sum(v) for v in zip(self.velocity, action)]
    self.restrict_velocity()

  def restrict_velocity(self, minimum=0, maximum=5):
    """  速度を制限する

    x, yともに0 - 5 の範囲内に収まるようにする。
    つまり下か右にしか進めないことに注意する。
    """
    self.velocity = [min(max(minimum, v), maximum) for v in self.velocity]

  def get_cell(self):
    return self.course.get_cell(self.position)

  def is_finish(self):
    cell = self.get_cell()
    return cell.__class__.__name__ == 'EndCell'

  def is_courseout(self):
    return not self.course.is_on_course(self.position)

  def is_cross_trajectory(self):
    """ 過去の軌跡を横切ってないか判定する

    そもそもこの速度の制約ではありえないはず。問題文の読み違えをしているかも
    """

    return False


class Result:
  """ S,A,Rの列を記録する
  """

  def __init__(self):
    self.sequence = []
    self.trajectory = []
  
  def record(self, r):
    self.sequence.append(r)

  def record_reward(self, r):
    self.record(r)
  
  def record_action(self, a):
    self.record(a)
  
  def record_state(self, s):
    self.record_trajectory(s)
    self.record(s)

  def record_trajectory(self, s):
    self.trajectory.append(s)

  def get_trajectory(self):
    """ S の推移から agent の辿った軌跡を表現する
    """

    return self.trajectory

