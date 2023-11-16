import unittest


from apex.assignment import n, N12, students_number, another_n, yet_another_n
from apex.extension import students_number as incr_students_number
from extension import students_number as incr_twice_students_number
from bunch.extension import students_number as decr_students_number

sample_list = ['a', 'b', 'c']

class AssignmentTest(unittest.TestCase):
    """The first and foremost to know"""

    def test_variables_vaues(self):
        self.assertEqual(n, 21)
        self.assertEqual(N12, 23.71)
        self.assertEqual(students_number, 233)


class ReassignmentTest(unittest.TestCase):
    """The set of pequiliar quirks"""

    def test_reassigned_variable_value(self):
        n = 22
        self.assertEqual(n, 22)

    def test_original_variable_value(self):
        self.assertEqual(n, 21)


class DataMutationTest(unittest.TestCase):
    """Who knows how it mutated"""

    def test_variables_vaues(self):
        self.assertEqual(n, 21)
        self.assertEqual(another_n, 27)
        self.assertEqual(yet_another_n, 28)

    # but in the same time:
    # immutable types: strings, ints, froats, tuples
    # and it is possible only ~to rebind~ thier values
    def test_mutability_inter_assigned_variables(self):
        self.n = n + 1
        self.assertEqual(self.n, 22)
        self.assertEqual(n, 21)

    # listst are mutable type, and it is possible to modify them
    # ~in place~:
    def test_innate_mutation_method_for_mutable_types(self):
        print(sample_list)
        alias_of_sample_list = sample_list
        sample_list.append('d')
        # naturally, thesis
        self.assertEqual(sample_list, ['a', 'b', 'c', 'd'])
        # unexpectedly, counter-intuitive, anti-thesis
        self.assertEqual(alias_of_sample_list, ['a', 'b', 'c', 'd'])

    # but it's possible ~to rebind~ value of mutable variable
    # =as well=
    def test_rebind_value_of_mutable_variable(self):
        # alias_of_sample_list = sample_list
        print(sample_list)
        sample_list = self.sample_list + ['d']
        self.assertEqual(sample_list, ['a', 'b', 'c', 'd'])
        self.assertEqual(alias_of_sample_list, ['a', 'b', 'c'])


class ImportValuesTest(unittest.TestCase):
    """Reuse already exising values"""

    def test_neighbours_vaues(self):
        self.assertEqual(incr_students_number, 234)

    def test_siblings_values(self):
        self.assertEqual(decr_students_number, 232)

    def test_parents_vaues(self):
        self.assertEqual(incr_twice_students_number, 235)
