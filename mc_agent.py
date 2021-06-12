import agent
import random

class On_Policy_MC_Agent(agent.Agent):
  def __init__(self, course, eps = 0.1):
    super().__init__(course)
    self.eps = eps
    all_cells = self.course.get_all_cell_list()
    self.gamma = 0.9

    # policy は deterministic に持っておく。初期値はランダム。
    self.policy = {cell: self.get_random_action() for cell in all_cells}
    self.count = {cell: {action: 0 for action in self.action_set} for cell in all_cells}
    self.Q = {cell: {action: 0 for action in self.action_set} for cell in all_cells}

  def learn(self, result):
    G = 0
    for sar in reversed(result.sequence):
      G = self.gamma*G + sar.reward
      if result.is_first_visit(sar):

        state = sar.state
        action = sar.action

        old = self.Q[state][action]
        self.count[state][action] += 1
        self.Q[state][action] = old + 1/self.count[state][action] * (G - old)

        # policy の更新
        Qs = self.Q[state]
        greedy_action = max(Qs, key=Qs.get)
        self.policy[state] = greedy_action # state と cell は同じオブジェクトを表すことに注意 TODO: バグの温床なので修正

  def select_action(self):
    if random.random() > self.eps: # greedy
      action = self.get_greedy_action()
    else: # explore
      action = self.get_random_action()

    return action
  
  def get_greedy_action(self):
    cell = self.get_cell(self.position)
    return self.policy[cell]
