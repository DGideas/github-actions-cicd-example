from unittest import TestCase

import a


class TestAdd(TestCase):
    def test_add(self):
        self.assertEqual(a.add(1, 2), 3)
        self.assertEqual(a.add(1, -1), 0)
