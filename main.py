import course as co
import agent as ag
import viewer as vi
import mc_agent as mc

import sys

def main():
  start_drawing_episode = int(sys.argv[1]) if len(sys.argv) > 1 else 0
  csv_flg = len(sys.argv) > 2

  cg = co.CourseGenerator()
  if csv_flg:
    course = cg.create_course_from_csv(sys.argv[2])
  else:
    course = cg.simple_course2()

  agent = mc.On_Policy_MC_Agent(course)
  # agent = ag.Agent(course)

  rl = RL(agent, 10**9)

  # TODO: マルチスレッドにしてRLとviewerを独立させたい
  viewer = vi.Viewer(rl, start_drawing_episode)

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