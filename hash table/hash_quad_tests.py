import unittest
from hash_quad import *


class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(6)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1 / 7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_02(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("o", 0)
        self.assertEqual(ht.get_index("o"), 3)
        ht.insert("v", 0)  # Causes rehash
        self.assertEqual(ht.get_index("a"), 12)
        self.assertEqual(ht.get_index("h"), 2)
        self.assertEqual(ht.get_index("o"), 9)
        self.assertEqual(ht.get_index("v"), 16)

    def test_03(self):
        ht = HashTable(5)
        for i in range(100):
            ht.insert(str(i), i)
        self.assertEqual(ht.get_table_size(), 397)

    def test_04(self):
        ht = HashTable(3)
        ht.insert('apple', 'banana')
        ht.insert('apple', 'orange')
        self.assertEqual(ht.get_value('apple'), 'orange')

    def test_05(self):
        ht = HashTable(6)
        self.assertEqual(ht.get_table_size(), 7)
        ht.insert('plum', 'grape')
        self.assertFalse(ht.in_table('grape'))

    def test_06(self):
        ht = HashTable(4)
        self.assertEqual(ht.get_table_size(), 5)
        ht.insert('watermelon', 'mango')
        self.assertEqual(ht.get_index('mango'), None)

    def test_07(self):
        ht = HashTable(98)
        self.assertEqual(ht.get_table_size(), 101)
        ht.insert('orange', 'juice')
        self.assertEqual(ht.get_value('juice'), None)

    def test_08(self):
        ht = HashTable(4)
        self.assertEqual(ht.get_table_size(), 5)
        ht.insert('abc', 100)
        self.assertEqual(ht.get_index('abc'), 4)
        ht.insert('cba', 100)
        self.assertEqual(ht.get_index('cba'), 0)
        ht.insert('bca', 100)
        self.assertEqual(ht.get_index('bca'), 5)

    def test_09(self):
        ht = HashTable(7)
        ht.insert('a', 1)
        ht.insert('h', 2)
        ht.insert('o', 3)
        self.assertEqual(ht.get_all_keys(), ['h', 'o', 'a'])
        ht.insert('o', 5)
        self.assertEqual(ht.get_value('o'), 5)

    def test_10(self):
        ht = HashTable(1)
        self.assertEqual(ht.get_table_size(), 2)

    def test_11(self):
        ht = HashTable(7)
        ht.insert('a', 1)
        ht.insert('h', 2)
        ht.insert('o', 3)
        self.assertEqual(ht.get_all_keys(), ['h', 'o', 'a'])
        ht.insert('o', 5)
        self.assertTrue(ht.in_table('o'))

    def test_12(self):
        ht = HashTable(5)
        ht.insert('b', 7)
        self.assertEqual(ht.get_value('m'), None)


if __name__ == '__main__':
    unittest.main()
