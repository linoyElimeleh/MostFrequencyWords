# Starting code
import math
from urllib.request import urlopen
from collections import Counter
import unittest


class MostFrequencyWords:

    def __init__(self, url, most_common_word_number):

        # Validation of vars
        self.validation_checking(most_common_word_number)

        # Steps
        data = self.read_file_by_url(url)
        words_list = self.initialize_words_list(data)
        word_counter_list = self.count_word_list(words_list)
        self.final_words_respond = self.get_most_common_word(word_counter_list, most_common_word_number)

    def validation_checking(self, most_common_word_number):
        if most_common_word_number < 0:
            raise Exception("Number frequency is not valid.")

    def read_file_by_url(self, url):
        try:
            with urlopen(url) as f:
                return f.read().decode("utf-8")
        except Exception as e:
            raise Exception("Error reading file from URL")

    def initialize_words_list(self, data):
        words_list = []
        lines = data.splitlines()
        for line in lines:
            words = line.split()
            for word in words:
                words_list.add(word)

        return words_list

    def count_word_list(self, words_list):
        return Counter(words_list)

    def get_most_common_word(self, word_counter_list, most_common_word_number):
        return word_counter_list.most_common(most_common_word_number)


class TestMostFrequencyWords(unittest.TestCase):
    # Todo add more test cases: white box to reading file, white box to get words list

    def setUp(self):
        # self.sample_url= "https://example-files.online-convert.com/document/txt/example.txt"
        self.sample_valid_url = "https://docs.google.com/document/d/1X2qHnT_jEu6yO9MntiJbwa8gnwMtt79PMoI5sfKvYT0/edit?usp=sharing"
        self.sample_invalid_url = "https://docs.google.com/document/d/blablalballinoyyyyy"
        self.most_common_word_number = 5

    def test_most_common_words_functionality_end_to_end(self):
        expected_most_common = [('a', 757), ('is', 755), ('nice', 752), ('language.', 728), ('Python', 631)]

        freq_counter = MostFrequencyWords(self.sample_valid_url, self.most_common_word_number)
        most_common_words = freq_counter.final_words_respond

        self.assertEqual(most_common_words, expected_most_common)

    def test_exception_when_negative_most_common_number(self):
        with self.assertRaises(Exception):
            negative_number = -1
            MostFrequencyWords(self.sample_valid_url, negative_number)

    def test_exception_when_getting_invalid_url(self):
        with self.assertRaises(Exception):
            MostFrequencyWords(self.sample_invalid_url, self.most_common_word_number)

    def test_getting_zero_results_most_common_number(self):
        zero_number = 0
        freq_counter = MostFrequencyWords(self.sample_valid_url, zero_number)
        most_common_words = freq_counter.final_words_respond

        self.assertEqual(most_common_words, [])

    def test_getting_the_most_common_word_white_box_component(self):
        word_list = ["Banana", "Apple", "Fish", "Banana", "Apple", "Python"]
        expected_most_common = [('Banana', 2), ('Apple', 2)]

        most_frequency_object = MostFrequencyWords(self.sample_valid_url, 2)
        word_counter = most_frequency_object.count_word_list(word_list)
        most_common_words = most_frequency_object.get_most_common_word(word_counter, 2)

        self.assertEqual(most_common_words, expected_most_common)

    def test_getting_the_word_list_counter_white_box_component(self):
        word_list = ["Banana", "Apple", "Fish", "Banana", "Apple", "Python"]
        expected_most_common = Counter({'Banana': 2, 'Apple': 2, 'Fish': 1, 'Python': 1})

        most_frequency_object = MostFrequencyWords(self.sample_valid_url, 2)
        word_counter = most_frequency_object.count_word_list(word_list)

        self.assertEqual(word_counter, expected_most_common)


if __name__ == '__main__':
    unittest.main()


class Calculator:

    def __init__(self):
        self.version = 1

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

    def square(self, x):
        x ** 2

    def root(self, x):
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(x)

