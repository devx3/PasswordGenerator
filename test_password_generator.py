"""
Funções
    Criar caractere especial baseado na tabela unicode
        Ranges: 32-47 58-64 91-96 123-126 -> [ -\\/:-@\\[-`{-~]
    Criar letras maiúsculas baseado na tabela unicode
        Ranges: 65-90
    Criar letras minúsculas baseado na tabela unicode
        Ranges: 97-122
    Criar números baseado na tabela unicode
        Ranges: 48-57

    Criar senha com:
        possibilidade de escolha dos caracteres (letras, números, etc)
        possibilidade de escolha do tamanho da senha (min = 4)
"""

from password_generator import \
    make_one_special_char, \
    make_one_uppercase_letter, \
    make_one_lowercase_letter, \
    make_one_number, \
    make_password
import unittest
import re


class TestPasswordGenerator(unittest.TestCase):

    def test_make_one_special_char_multiple_ranges(self):
        regex = re.compile(r'^[ -\/:-@\[-`{-~]$')
        for i in range(100):
            with self.subTest(i=i):
                self.assertRegex(make_one_special_char(), regex)

    def test_make_one_uppercase_letter_65_90(self):  # Outra forma de validar
        ord_range = list(range(65, 91))  # Ultimo elemento é eliminado do range
        # regex = re.compile(r'^[A-Z]$')
        for i in range(100):
            with self.subTest(i=i):
                self.assertIn(ord(make_one_uppercase_letter()), ord_range)

    def test_make_one_lowercase_letter_97_122(self):
        regex = re.compile(r'^[a-z]$')
        for i in range(100):
            with self.subTest(i=i):
                self.assertRegex(make_one_lowercase_letter(), regex)

    def test_make_one_number_48_57(self):
        regex = re.compile(r'^[0-9]$')
        for i in range(100):
            with self.subTest(i=i):
                self.assertRegex(make_one_number(), regex)

    def test_make_password(self):
        with self.assertRaises(AssertionError):
            make_password(length=1)

        with self.assertRaises(AssertionError):
            make_password(length='a')

        for i in range(4, 100):
            with self.subTest(i=i):
                self.assertTrue(len(make_password(length=i)) == i)

    def test_make_password_all_params_true(self):
        regex = re.compile(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@\[-`{-~]).+$'
        )
        self.assertRegex(make_password(), regex)

    def test_make_password_all_params_false(self):
        with self.assertRaises(AssertionError):
            make_password(numbers=False, upper=False, lower=False, chars=False)

    def test_make_password_no_upper(self):
        regex = re.compile(r'^[^A-Z]+$')

        for i in range(4, 100):
            self.assertRegex(make_password(upper=False), regex)

    def test_make_password_no_lower(self):
        regex = re.compile(r'^[^a-z]+$')

        for i in range(4, 100):
            self.assertRegex(make_password(lower=False), regex)

    def test_make_password_no_numbers(self):
        regex = re.compile(r'^\D+$')

        for i in range(4, 100):
            self.assertRegex(make_password(numbers=False), regex)

    def test_make_password_no_special_chars(self):
        regex = re.compile(r'^[^ -\/:-@\[-`{-~]+$')

        for i in range(4, 100):
            self.assertRegex(make_password(chars=False), regex)

    def test_make_password_sequence_not_allowed(self):
        regex = re.compile(r'^(?:[ -\/:-@\[-`{-~][a-z][A-Z][0-9])+&')

        for i in range(4, 10):
            with self.subTest(i=i):
                self.assertNotRegex(make_password(length=i), regex)


if __name__ == "__main__":
    unittest.main(verbosity=2)
