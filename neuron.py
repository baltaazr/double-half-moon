import random


class Neuron:
    def __init__(self, n):
        w = []
        w.append(random.random())
        for i in range(n):
            w.append(random.random())
        self.w = w
        self.learningRate = 0.1

    def activate(self, x):
        x = x.copy()
        x.insert(0, -1)
        result = 0
        for i in range(0, len(self.w)):
            result += x[i] * self.w[i]
        return result > 0

    def train(self, trainingSet, max_iter, cur_iter=1):
        trainingSet = trainingSet.copy()
        random.shuffle(trainingSet)
        error = 0
        for x in trainingSet:
            t = x[2]
            o = -1
            if self.activate(x):
                o = 1
            else:
                o = 0
            error += abs(t-o)
            x = x.copy()
            x.insert(0, -1)
            for i in range(0, len(self.w)):
                self.w[i] += self.learningRate*(t-o)*x[i]
        if(error == 0 or cur_iter >= max_iter):
            return
        else:
            self.train(trainingSet, max_iter, cur_iter+1)
