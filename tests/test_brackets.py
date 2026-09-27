import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from brackets import brackets_balanced, first_mismatch, mismatch_kind


class TestBrackets(unittest.TestCase):
    def test_cases(self) -> None:
        self.assertTrue(brackets_balanced(""))
        self.assertTrue(brackets_balanced("()"))
        self.assertTrue(brackets_balanced("([])"))
        self.assertTrue(brackets_balanced("[()]()"))
        self.assertFalse(brackets_balanced("([)]"))
        self.assertFalse(brackets_balanced("(("))
        self.assertFalse(brackets_balanced(")"))
        self.assertTrue(brackets_balanced("{[()]}"))
        self.assertFalse(brackets_balanced("{[}]"))
        self.assertIsNone(first_mismatch("([])"))
        self.assertEqual(first_mismatch("([)]"), 2)
        self.assertEqual(first_mismatch("(("), 0)
        self.assertEqual(first_mismatch(")"), 0)
        self.assertEqual(mismatch_kind("([])"), "ok")
        self.assertEqual(mismatch_kind("([)]"), "closer")
        self.assertEqual(mismatch_kind("(("), "open")


if __name__ == "__main__":
    unittest.main()
