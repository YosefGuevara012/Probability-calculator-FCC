import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, extracted):
    contents = []
    if extracted > len(self.contents):
      return self.contents
    else:
      for i in range(extracted):
        choise = random.choice(self.contents)
        contents.append(choise)
        self.contents.remove(choise)

      #print(contents)
      return contents
  

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  M = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    #print(hat_copy.contents)
    actual_balls = hat_copy.draw(num_balls_drawn)
    # print(actual_balls)
    attempt = 1
    for key,value in expected_balls.items():
      if actual_balls.count(key) >= value:
        attempt *=  1
      else:
        attempt *= 0
    
    # print(attempt)
    
    if attempt == 1:
      M += 1
    else:
      M += 0

  # print(M)
  return M/num_experiments
