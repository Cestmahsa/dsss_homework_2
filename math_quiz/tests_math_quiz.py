import unittest
from math_quiz import generate_random_integer, generate_random_operator, perform_operation


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_value, max_value)
            self.assertTrue(min_value <= rand_num <= max_value)

    def test_generate_random_operator(self):
        # TODO
        operators = set(['+', '-', '*'])
        rand_operator = generate_random_operator()
        self.assertIn(rand_operator, operators)

    def test_perform_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
                (3, 4, '*', '3 * 4', 12),
                (8, 3, '-', '8 - 3', 5),
        ]
        
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                problem, result = perform_operation(num1, num2, operator)

                # Check if the generated problem and result match the expected values
                self.assertEqual(problem, expected_problem)
                self.assertEqual(result, expected_answer)

if __name__ == "__main__":
    unittest.main()
