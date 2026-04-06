import unittest
import sys
import os

# Добавляем путь к модулю
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processor import process_numbers, process_string


class TestDataProcessor(unittest.TestCase):

    def test_process_numbers_sum(self):
        result = process_numbers([1, 2, 3, 4])
        self.assertEqual(result["sum"], 10)

    def test_process_numbers_empty(self):
        result = process_numbers([])
        self.assertEqual(result, {"error": "Список чисел пуст"})

    def test_process_string_length(self):
        result = process_string("Hello")
        self.assertEqual(result["length"], 5)

    def test_process_string_empty(self):
        result = process_string("")
        self.assertEqual(result, {"error": "Строка пустая"})


if __name__ == '__main__':
    unittest.main(verbosity=2)
