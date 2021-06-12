import random
import itertools
import action as ac
import result as re

class Agent:
  def __init__(self, course):
    self.position = [0,0] #仮
    self.former_position = self.position # TODO: なくてもvelocityで代用できるので消す
    ag = ac.ActionGenerator()
    self.action_set = ag.simple_action_set()
    
    # agent が course に対しての知識を持つべきではないか？
    self.course = course
  
  def initialize(self):
    """ エピソード開始時の初期化
    """

    self.move_to_start()
    self.velocity = [0,0]
    self.first = True

  def go(self):
    """ 1エピソード分行動する
    """
    self.initialize()

    result = re.Result()

    while True:
      
      if self.is_courseout() or self.is_cross_trajectory():
        self.move_to_start()

      if self.is_finish():
        result.record_sar(s,action,0)
        break


      if not self.first:
        result.record_sar(s,action,-1)

      s = self.get_cell(self.position)
      action = self.select_action()
      self.apply_action(action)
      self.move()

      self.first = False
    
    return result

  def learn(self, result):
    print('learn')
    pass

  def move(self):
    self.former_position = self.position
    self.position = [sum(p) for p in zip(self.position, self.velocity)]

  def move_to_start(self):
    """ ランダムなスタート地点に移動する。

    former_position も変更する。
    """

    cell = self.course.get_random_start_cell()
    self.position = [cell.x, cell.y]
    self.former_position = self.position

  def select_action(self):
    # ランダムポリシーに対応するやつ。仮置き
    action = random.sample(self.action_set, 1)[0]

    return action

  def apply_action(self, action):
    self.velocity = [sum(v) for v in zip(self.velocity, action.value)]
    self.restrict_velocity()

  def restrict_velocity(self, minimum=0, maximum=5):
    """  速度を制限する

    x, yともに0 - 5 の範囲内に収まるようにする。
    つまり下か右にしか進めないことに注意する。
    """
    self.velocity = [min(max(minimum, v), maximum) for v in self.velocity]

  def get_cell(self, pos):
    return self.course.get_cell(pos)

  def is_finish(self):
    """ ゴールしたかどうかを確認する。
    """

    cells = self.course.get_cells_betwenn_two_position(self.former_position, self.position)

    return any(cell.is_finish() for cell in cells)
  
  def is_finish_cell(self, pos):
    cell = self.get_cell(pos)
    return cell.__class__.__name__ == 'EndCell'

  def is_courseout(self):
    return not self.course.is_on_course(self.position)

  def is_cross_trajectory(self):
    """ 過去の軌跡を横切ってないか判定する

    そもそもこの速度の制約ではありえないはず。問題文の読み違えをしているかも
    """

    return False