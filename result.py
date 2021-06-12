class Result:
  """ S,A,Rの列を記録する
  """

  def __init__(self):
    self.sequence = []
    self.trajectory = []
    self.count = 0

  def record_sar(self, s, a, r):
    self.count += 1
    self.sequence.append(SAR(s, a, r, self.count))

    self.record_trajectory(s)

  def record_trajectory(self, s):
    self.trajectory.append(s)

  def get_trajectory(self):
    """ S の推移から agent の辿った軌跡を表現する
    """

    return self.trajectory

  def is_first_visit(self, sar):
    """ SAR の組に対して、SAが初めて登場したかを調べる
    """

    count = sar.time

    if count == 1:
      return True

    for target in self.sequence[:count-1]:
      if sar.is_same_sa(target):
        return False
    return True

class SAR:
  """ ある時刻における state action reward の組を記録する

  教科書とは reward の時間をずらしていることに注意
  つまり、 s_t, a_t, r_{t+1}, s_{t+1}, ...　と教科書ではなっているが.
  s_t, a_t, r_t, s_{t+1}, ... として扱う
  """

  def __init__(self, state, action, reward, time):
    self.state = state
    self.action = action
    self.reward = reward
    self.time = time
  
  def is_same_sa(self, target):
    """ sa の組が同じかどうか調べる
    """

    return self.action == target.action and self.state == target.state