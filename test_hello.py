import hello
import unittest

class PrintsHello(unittest.TestCase):
    correct_output = 'Hello world!'

    def test_output(self):
        output = hello.hello_world()
        self.assertEqual(output, self.correct_output)

if __name__ == '__main__':
    unittest.main()