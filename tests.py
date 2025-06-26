from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

import unittest

'''
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
'''
class TestGetFileContent(unittest.TestCase):
    def test_get_file_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)

    def test_get_file_pkg(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)

    def test_get_file_no_permission(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)

#    def test_get_lorem(self):
#        result = get_file_content("calculator", "lorem.txt")
#        print(result)

def main():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)
    
if __name__ == "__main__":
    main()