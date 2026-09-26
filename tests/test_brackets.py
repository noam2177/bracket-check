import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from brackets import brackets_balanced


class TestBrackets(unittest.TestCase):
    def test_cases(self) -> None:
        self.assertTrue(brackets_balanced(""))
        self.assertTrue(brackets_balanced("()"))
        self.assertTrue(brackets_balanced("([])"))
        self.assertTrue(brackets_balanced("[()]()"))
        self.assertFalse(brackets_balanced("([)]"))
        self.assertFalse(brackets_balanced("(("))
        self.assertFalse(brackets_balanced(")"))


if __name__ == "__main__":
    unittest.main()
