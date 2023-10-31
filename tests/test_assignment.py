import unittest


from apex.assignment import n, N12, students_number


class AssignmentTest(unittest.TestCase):
    """The first and foremost to know"""

    def test_variables_vaues(self):
        self.assertEqual(n, 21)
        self.assertEqual(N12, 23.71)
        self.assertEqual(students_number, 233)

    def test_reassign_variable_value(self):
        n = 22
        self.assertEqual(n, 22)

    def test_original_variable_value(self):
        self.assertEqual(n, 21)
