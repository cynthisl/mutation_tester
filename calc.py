
class Calculator(object):
    def add(self, x, y):
        return x+y

    def mul(self, x, y):
        return x*y

    def random(self):
        return 4

    def sliced(self, l, pos):
        m = l[:pos]
        return m

    def equality(self, a, b):
        if a == b:
            return "yes"
        else:
            return "no"


class SuperCalculator(Calculator):
    def __init__(self):
        Calculator.__init__(self)

    def random(self):
        return "random"
