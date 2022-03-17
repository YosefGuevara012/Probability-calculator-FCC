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

      print(contents)
      return contents
    
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pass
