import unittest

import forward_index
import inverted_index


class TestForwardIndex(unittest.TestCase):
    def test_forward_index_with_one_word(self):
        text = 'Bird'
        result = forward_index.generate_forward_index(text)
        self.assertEqual(result, ['bird'])

    def test_forward_index_multiple_words(self):
        text = 'For most seagulls life consists simply of eating and surviving'
        result = forward_index.generate_forward_index(text)
        self.assertEqual(['and', 'consists', 'eating', 'for', 'life', 'most', 'of', 'seagulls', 'simply', 'surviving'],
                         result)

    def test_forward_index_with_duplicates(self):
        text = 'Jonathan nodded obediently to Jonathan'
        result = forward_index.generate_forward_index(text)
        self.assertEqual(result, ['jonathan', 'nodded', 'obediently', 'to'])

    def test_forward_index_empty(self):
        text = ''
        result = forward_index.generate_forward_index(text)
        self.assertEqual(result, [''])


class TestInvertedIndex(unittest.TestCase):
    def test_inverted_index_with_one_word(self):
        text = 'Seagull'
        index = {
            'jonathan': ['text1']
        }
        result = inverted_index.generate_inverted_index(text, index, 'text2')
        self.assertEqual(result, {
            'seagull': ['text2'],
            'jonathan': ['text1']
        })

    def test_inverted_index_with_multiple_words(self):
        text = 'Jonathan was a seagull'
        index = {
            'seagull': ['text1']
        }
        result = inverted_index.generate_inverted_index(text, index, 'text2')
        self.assertDictEqual(result, {
            'jonathan': ['text2'],
            'was': ['text2'],
            'a': ['text2'],
            'seagull': ['text1', 'text2']
        })

    def test_inverted_index_empty(self):
        text = ''
        result = {
            'livingston': ['text1']
        }
        inverted_index.generate_inverted_index(text, result, 'text2')
        self.assertEqual(result, {
            'livingston': ['text1']
        })


class TestSearchForward(unittest.TestCase):
    def test_search_forward_present_in_one(self):
        index = {
            'text1': ['he', 'pushed', 'wearily', 'away'],
            'text2': ['another']
        }
        result = forward_index.search_forward_index(index, 'away')
        self.assertEqual(result, ['text1'])

    def test_search_forward_present_in_many(self):
        index = {
            'text1': ['collision', 'would', 'be', 'instant', 'death'],
            'text2': ['thinking', 'of', 'death']
        }
        result = forward_index.search_forward_index(index, 'death')
        self.assertEqual(result, ['text1', 'text2'])

    def test_search_forward_not_present(self):
        index = {
            'data_1': ['it', 'happened', 'that', 'morning'],
            'data_2': ['morning', 'sunshine'],
        }
        result = forward_index.search_forward_index(index, 'bird')
        self.assertEqual(result, [])


class TestSearchInverted(unittest.TestCase):
    def test_search_inverted_present_in_one(self):
        index = {
            'seagull': ['text1'],
            'bird': ['text2'],
        }
        result = inverted_index.search_inverted_index(index, 'seagull')
        self.assertEqual(result, ['text1'])

    def test_search_inverted_present_in_many(self):
        index = {
            'seagull': ['text1', 'text2'],
            'bird': ['text3'],
        }
        result = inverted_index.search_inverted_index(index, 'seagull')
        self.assertEqual(result, ['text1', 'text2'])

    def test_search_inverted_not_present(self):
        index = {
            'jonathan': ['text2'],
            'livingston': ['text1', 'text2'],
        }
        result = inverted_index.search_inverted_index(index, 'bird')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
