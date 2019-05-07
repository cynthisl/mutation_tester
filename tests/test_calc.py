from calc import Calculator

class TestCalculator:

    def test_add(self):
        c = Calculator()
        assert c.add(2,2) == 4

    def test_mul(self):
        c = Calculator()
        assert c.mul(2,2) == 4

    def test_random(self):
        c = Calculator()
        assert c.random() == 4
