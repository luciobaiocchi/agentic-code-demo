# tests.py

import unittest
from functions.get_files_info import get_files_info


class TestCalculator(unittest.TestCase):
    def setUp(self):
        print("testing functions")

    def test_get_file_info(self):
        print(get_files_info("calculator", "."))
        print(get_files_info("calculator", "pkg"))
        print(get_files_info("calculator", "/bin"))
        print(get_files_info("calculator", "../"))



if __name__ == "__main__":
    unittest.main()