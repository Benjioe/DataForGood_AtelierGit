import unittest

from main import IsWorking

# python -m unittest -v test.TestIsWorking.should_return_true
class TestIsWorking(unittest.TestCase):
    def should_return_true(self):
        self.assertTrue(IsWorking())

if __name__ == "__main__":
    unittest.main()