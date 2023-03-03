import unittest
from helloworld import get_greetings

class HelloworldTests(unittest.TestCase):

    def test_get_helloworld(self):
        self.assertEqual(get_greetings(),'Hello world')

if __name__ == '__main__':
    unittest.main()