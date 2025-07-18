import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from gradechecker import GradeList, Category
import unittest

class TestGrades(unittest.TestCase):
    def test_discrete_math(self):
        print()
        print('Test Starting: Applied Discrete Math...')
        DiscreteMath = GradeList()
        DiscreteMath.addCategory("Quizzes", 40, 178.8, 200)
        DiscreteMath.addCategory("Homework", 20, 491.6, 508.00)
        DiscreteMath.addCategory("Lab", 15, 60, 60)
        DiscreteMath.addCategory("Final", 25, 84, 100)

        DiscreteMath.calculateGrade()
        result = DiscreteMath.total
        self.assertEqual(str(round(result, 2)), "91.11")
        DiscreteMath.print()

    def test_incomplete(self):
        print()
        print('Test Starting: Incomplete Discrete Math...')
        DiscreteMath = GradeList()
        DiscreteMath.addCategory("Quizzes", 40, 178.8, 200)
        DiscreteMath.addCategory("Homework", 20, 491.6, 508.00)
        DiscreteMath.addCategory("Lab", 15, 60, 60)

        DiscreteMath.calculateGrade()
        result = DiscreteMath.total
        DiscreteMath.print()
        self.assertEqual(str(round(result, 2)), "93.49")

    def test_empty_category(self):
        print()
        print('Test Starting: Empty Discrete Math Final...')
        DiscreteMath = GradeList()
        DiscreteMath.addCategory("Quizzes", 40, 178.8, 200)
        DiscreteMath.addCategory("Homework", 20, 491.6, 508.00)
        DiscreteMath.addCategory("Lab", 15, 60, 60)
        DiscreteMath.addCategory("Final", 25, 0, 0)

        DiscreteMath.calculateGrade()
        result = DiscreteMath.total
        DiscreteMath.print()
        self.assertEqual(str(round(result, 2)), "93.49")

    def test_extra_credit(self):
        pass
        

if __name__ == "__main__":
    unittest.main()
