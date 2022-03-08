import unittest
from unittest.mock import patch
from main import *
import datetime
import random, string
from main import *
def random_string():
   length = random.randrange(0,30)
   letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
   return ''.join(random.choice(letters) for i in range(length))

test = [random_string(), random_string(), None, None, 'megasupertest', '']
display = Display()
class TestStringMethods(unittest.TestCase):

    @patch('builtins.input', side_effect=test)
    def test_creator(self, mock):
        for i in range(len(test)//2):
            display.create_note()
            num = (i//2)
            self.assertEqual(NOTEBOOK.notes[num+1].memo, test[num*2])
            self.assertEqual(NOTEBOOK.notes[num+1].tags, test[1+num*2])
            self.assertEqual(NOTEBOOK.notes[num+1].id, num+1)

    @patch('builtins.input', side_effect=[1, None, 'test'])
    def test_modifier(self, mock):
        memo = NOTEBOOK.notes[1].memo
        display.modify_note()
        self.assertEqual(NOTEBOOK.notes[1].memo, memo)
        self.assertEqual(NOTEBOOK.notes[1].tags, 'test')
        self.assertEqual(NOTEBOOK.notes[1].id, 1)

    def test_filter(self):
        self.assertEqual(NOTEBOOK.search("test")[0].memo,'megasupertest')      

if __name__ == '__main__':
    unittest.main()