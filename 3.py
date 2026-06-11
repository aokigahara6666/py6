import sys
import unittest

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result


class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_overflow(self):
        with self.assertRaises(ValueError):
            factorial(100000)


if __name__ == "__main__":
    unittest.main()