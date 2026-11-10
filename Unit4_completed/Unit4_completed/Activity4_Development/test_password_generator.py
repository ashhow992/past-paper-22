import unittest
import string
from password_generator import generate_password


class PasswordTests(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(generate_password()), 16)

    def test_minimum_length(self):
        self.assertEqual(len(generate_password(4)), 4)

    def test_maximum_length(self):
        self.assertEqual(len(generate_password(128)), 128)

    def test_required_groups(self):
        value = generate_password(20)
        self.assertTrue(any(c.islower() for c in value))
        self.assertTrue(any(c.isupper() for c in value))
        self.assertTrue(any(c.isdigit() for c in value))
        self.assertTrue(any(c in '!@#$%^&*()-_=+[]{}?' for c in value))

    def test_only_digits(self):
        value = generate_password(12, False, False, True, False)
        self.assertTrue(all(c in string.digits for c in value))

    def test_invalid_lengths(self):
        for length in (0, 3, 129, -1):
            with self.subTest(length=length), self.assertRaises(ValueError):
                generate_password(length)

    def test_no_categories(self):
        with self.assertRaises(ValueError):
            generate_password(10, False, False, False, False)

    def test_non_integer_length(self):
        with self.assertRaises(TypeError):
            generate_password('16')

    def test_varied_outputs(self):
        self.assertNotEqual(generate_password(32), generate_password(32))


if __name__ == '__main__':
    unittest.main()
