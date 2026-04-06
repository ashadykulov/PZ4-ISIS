import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processor import input_numbers, process_numbers, process_string


class TestDataProcessor(unittest.TestCase):

    @patch('builtins.input', return_value="1 2 3 4")
    def test_input_numbers_valid(self, mock_input):
        self.assertEqual(input_numbers(), [1, 2, 3, 4])

    @patch('builtins.input', return_value="")
    def test_input_numbers_empty(self, mock_input):
        self.assertEqual(input_numbers(), [])

    def test_process_numbers_valid(self):
        result = process_numbers([1, 2, 3, 4])
        self.assertEqual(result["sum"], 10)
        self.assertEqual(result["average"], 2.5)

    def test_process_numbers_empty(self):
        result = process_numbers([])
        self.assertEqual(result, {"error": "Список чисел пуст"})

    def test_process_string_empty(self):
        result = process_string("")
        self.assertEqual(result, {"error": "Строка пустая"})


if __name__ == '__main__':
    unittest.main(verbosity=2)import unittest
from unittest.mock import patch
import sys
import os

# Добавляем корень проекта в путь
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processor import input_numbers, process_numbers, process_string


class TestDataProcessor(unittest.TestCase):

    @patch('builtins.input', return_value="1 2 3 4")
    def test_input_numbers_valid(self, mock_input):
        self.assertEqual(input_numbers(), [1, 2, 3, 4])

    @patch('builtins.input', return_value="")
    def test_input_numbers_empty(self, mock_input):
        self.assertEqual(input_numbers(), [])

    @patch('builtins.input', return_value="5 abc 7")
    def test_input_numbers_invalid(self, mock_input):
        self.assertEqual(input_numbers(), [])

    def test_process_numbers_valid(self):
        result = process_numbers([1, 2, 3, 4])
        self.assertEqual(result["sum"], 10)
        self.assertEqual(result["average"], 2.5)
        self.assertEqual(result["max"], 4)
        self.assertEqual(result["min"], 1)

    def test_process_numbers_empty(self):
        result = process_numbers([])
        self.assertEqual(result, {"error": "Список чисел пуст"})

    def test_process_string_valid(self):
        result = process_string("Hello World")
        self.assertEqual(result["length"], 11)
        self.assertEqual(result["uppercase"], "HELLO WORLD")

    def test_process_string_empty(self):
        result = process_string("")
        self.assertEqual(result, {"error": "Строка пустая"})


if __name__ == '__main__':
    unittest.main(verbosity=2)
