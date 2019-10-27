import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		rpn.calculate("1")
		rpn.calculate("1")
		rpn.calculate("+")
		self.assertEqual(2, rpn.answer())


