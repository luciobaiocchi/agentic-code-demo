# tests.py

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


class TestCalculator(unittest.TestCase):
    def setUp(self):
        print("testing functions")

    '''
    def test_get_file_list(self):
        print(get_files_info("calculator", "."))
        print(get_files_info("calculator", "pkg"))
        print(get_files_info("calculator", "/bin"))
        print(get_files_info("calculator", "../"))
    '''
    
    '''
    def test_get_file_info(self):
        print(get_file_content("calculator", "main.py"))
        print(get_file_content("calculator", "pkg/calculator.py"))
        print(get_file_content("calculator", "/bin/cat"))
        print(get_file_content("calculator", "pkg/does_not_exist.py"))
        #print(get_file_content("calculator", "lorem.txt"))
    '''
    def test_get_file_info(self):
        print(write_file("./calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
        print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
        print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


if __name__ == "__main__":
    unittest.main()