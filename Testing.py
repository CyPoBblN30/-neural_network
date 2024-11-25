from unittest import TestCase


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


class TestFuncs(TestCase):
    def test_green1(self):
        return self.assertEqual(addition(1, 1), 2, 'Неверное сложение')

    def test_green2(self):
        return self.assertEqual(subtraction(2, 1), 1, 'Неверное вычетание')

    def test_green3(self):
        return self.assertEqual(multiplication(2, 2), 4, 'Неверное произведение')

    def test_green4(self):
        return self.assertEqual(division(6, 3), 2, 'Неверное деление')

    def test_red1(self):
        return self.assertEqual(addition(1, 1), 3, 'Неверное сложение')

    def test_red2(self):
        return self.assertEqual(subtraction(2, 1), 2, 'Неверное вычетание')

    def test_red3(self):
        return self.assertEqual(multiplication(2, 2), 5, 'Неверное произведение')

    def test_red4(self):
        return self.assertEqual(division(6, 3), 3, 'Неверное деление')




