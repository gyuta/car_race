import course as co
import agent as ag
import viewer as vi
import mc_agent as mc

def main():
  cg = co.CourseGenerator()
  course = cg.simple_course2()

  agent = mc.On_Policy_MC_Agent(course)
  # agent = ag.Agent(course)

  rl = RL(agent, 10**5)

  # TODO: マルチスレッドにしてRLとviewerを独立させたい
  viewer = vi.Viewer(rl)

  viewer.root.mainloop()

class RL:
  def __init__(self, agent, max_episode = 10**2):
    self.agent = agent
    self.max_episode = max_episode

  def do_episode(self):
    """ 一回分のエピソードを行う
    """

    result = self.agent.go()
    self.agent.learn(result)

    return result.get_trajectory()

if __name__ == '__main__':
  main()