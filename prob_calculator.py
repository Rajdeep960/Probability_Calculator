import random
import copy

class Hat:

    def __init__(self, **balls):
        self.contents = list()
        for key, value in balls.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num_of_balls):
        result = []
        if num_of_balls >= len(self.contents):
            result = self.contents
            return result
        else :
            for i in range(num_of_balls):
                random_number = random.randrange(len(self.contents))
                value = self.contents.pop(random_number)
                result.append(value)
            return result



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_list = []
    for key, value in expected_balls.items():
        for i in range(value):
            expected_balls_list.append(key)
    N = num_experiments
    M = 0

    for i in range(N):
        copyhat = copy.deepcopy(hat)
        result = copyhat.draw(num_balls_drawn)
        success=False
        for i in expected_balls_list:
            if expected_balls_list.count(i) <= result.count(i):
                success = True              
            else :
                success = False 
                break
    
        if success:
            M += 1
    return M/N


