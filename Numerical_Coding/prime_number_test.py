import unittest
from prime_number_count import check_prime


class PrimeTest(unittest.TestCase):
    def test_check_prime(self):
        # pass
        # Arrange
        a = 10
        b = 20

        # Act
        result = check_prime(10)

        self.assertEqual(result, True, "Not Match")
        # Assert


if __name__ == '__main__':
    unittest.main()
