class Action:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.value = [x,y]
    self.tag = f"{x} {y}"

class ActionGenerator:
  def __init__(self):
    pass

  def simple_action_set(self):
    """ x,y それぞれ [-1, 0, 1] の計９通りのアクションのセットをつくる 
    """

    res = set()
    for x in [-1, 0 ,1]:
      for y in [-1, 0, 1]:
        res.add(Action(x,y))
    
    return res
  