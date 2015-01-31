__author__ = 'xtofl'

class MasterMind:

    def __init__(self, random):
        self.random = random


    def start(self):
        self.secret = [self.random() for _ in range(4)]


    def guess(self, sequence):
        if sequence == self.secret:
            return (4, 0)
        else:
            right_place = sum(1 for (c, s) in zip(self.secret, sequence) if c == s)
            right_color = sum(1 for (c, s) in zip(self.secret, sequence) if s in self.secret and c != s)
            return (right_place, right_color)