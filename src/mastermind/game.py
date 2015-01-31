from random import randint, choice

__author__ = 'xtofl'

class MasterMind(object):

    def __init__(self, random):
        self.secret = MasterMind.make_secret(random)

    @staticmethod
    def make_secret(source):
        secret = []
        it = iter(source)
        for _ in range(4):
            n = next(it)
            while n in secret:
                n = next(it)
            secret.append(n)

        return secret


    def guess(self, sequence):
        if sequence == self.secret:
            return (4, 0)
        else:
            right_place = sum(1 for (c, s) in zip(self.secret, sequence) if c == s)
            right_color = sum(1 for (c, s) in zip(self.secret, sequence) if s in self.secret and c != s)
            return (right_place, right_color)




def validate(g):
    if any(not g in range(1, 9) for g in guess):
        raise ValueError()


def series():
    while True:
        yield choice(range(1, 9))

if __name__ == "__main__":
    game = MasterMind(random=series())

    for guess_nr in range(8):
        try:
            guess = [int(c) for c in raw_input("guess: ")]
            validate(guess)
            print(game.guess(guess))
            if game.guess(guess) == (4, 0):
                print("Gewonnen!")
                break
        except ValueError:
            print("bad input - only digits 12345678 allowed")

    print("lost... the combination was {}".format(game.secret))