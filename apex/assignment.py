# This is a cornerstone of any programming language. Python definetely
# ain't and exclusion out from general rule, but it has several
# pequiliar subtleties which you should to know.

# Comments are crucially required to humans to understand the author's
# idea and they begin with hash symbol; Python ignores them, they are
# only for humans

# The list of cornerstone of programming:
# 1. Assignment;
# 2. Flow control;
# 3. Extension;

# Assignment:
# <variable_name> = <value> <--this is a sample of assignment in general

n = 21  # <--the particular example with name and its integer value
N12 = 23.71  # <--the longer valid name for variable and its value with
# fractional part
students_number = 233  # <-- the long name is a basement for clarity


# special data for test hypothesis of immutability
another_n = n
yet_another_n = another_n
# assignment never copies data
another_n = 27
yet_another_n = 28
