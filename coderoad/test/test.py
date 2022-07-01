import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import unittest
import task

class Test(unittest.TestCase):
    def test_isZero(self):
        self.assertEqual(task.var, 0)

if __name__ == '__main__':
    unittest.main()