import random
import copy

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            setattr(self, key, value)
            self.contents += [key] * value

    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            return self.contents
        else:
            drawn_balls = []
            for _ in range(num_balls_drawn):
                random_element = random.choice(self.contents)
                drawn_balls.append(random_element)
                self.contents.remove(random_element)
            return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        condition = []
        for key, value in expected_balls.items():
            if drawn_balls.count(key) >= value:
                condition.append(1)

        if sum(condition) == len(expected_balls):
            m += 1
        else:
            m += 0

    return m / num_experiments
