from functions.get_files_info import get_files_info

import unittest

class TestGetFiles(unittest.TestCase):
    def test_calculator_files_all(self):
        result = get_files_info("calculator", ".")

        expected =\
"""- main.py: file_size=575 bytes, is_dir=False
- tests.py: file_size=1341 bytes, is_dir=False
- pkg: file_size=4096 bytes, is_dir=True"""

        print(result)
        self.assertEqual(result, expected)

    def test_calculator_dir_pkg(self):
        result = get_files_info("calculator", "pkg")
        expected =\
"""- __pycache__: file_size=4096 bytes, is_dir=True
- calculator.py: file_size=1737 bytes, is_dir=False
- render.py: file_size=766 bytes, is_dir=False"""

        print(result)
        self.assertEqual(result, expected)

    def test_calculator_dir_bin(self):
        directory = "/bin"
        result = get_files_info("calculator", directory)
        error_str = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        print(result)
        self.assertEqual(result, error_str)

    def test_calculator_no_permission(self):
        directory = "../"
        result = get_files_info("calculator", directory)
        error_str = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        print(result)
        self.assertEqual(result, error_str)
        
    def test_invalid_working_directory(self):
        working_directory = "calc"
        result = get_files_info(working_directory, ".")
        error_str = f'Error: "{working_directory}" is not a directory'

        print(result)
        self.assertEqual(result, error_str)

if __name__ == "__main__":
    unittest.main()