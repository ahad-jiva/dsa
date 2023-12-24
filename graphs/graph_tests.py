import unittest
from graph import *


class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        self.assertTrue(g.is_bipartite())

    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_empty(self):
        g = Graph('test_empty.txt')
        self.assertEqual(g.get_vertex('v1'), None)
        self.assertEqual(g.get_vertices(), [])
        self.assertEqual(g.conn_components(), [])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.conn_components(), [])
        self.assertTrue(g.is_bipartite())

    def test_03(self):
        g = Graph('test3.txt')
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7'])
        v3_adj = g.graph['v3']
        self.assertEqual(g.get_vertex('v3'), v3_adj)
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7']])
        self.assertFalse(g.is_bipartite())
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7']])
        self.assertFalse(g.is_bipartite())


if __name__ == '__main__':
    unittest.main()
