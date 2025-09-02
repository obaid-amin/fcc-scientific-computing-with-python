import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for color,count in kwargs.items():
            self.contents.extend([color] * count)
    def draw(self,num):
        drawn=[]
        if num >= len(self.contents):
            drawn=self.contents[:]
            self.contents.clear()
            return drawn
        else:
            for i in range(num):
                pick=random.choice(self.contents)
                self.contents.remove(pick)
                drawn.append(pick)
            return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    prob=num_experiments
    plus=0
    for k in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        dit = {}
        for i in hat_copy.draw(num_balls_drawn):
            if i in dit:
                dit[i] += 1
            else:
                dit[i] = 1

        success = True
        for color, count in expected_balls.items():
            if dit.get(color, 0) < count:
                success = False
                break
        if success:
            plus += 1


    prob=plus/prob
    return prob




hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(hat1.draw(11))