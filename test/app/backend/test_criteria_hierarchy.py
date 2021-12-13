import unittest

from app.backend.criteria_hierarchy import TreeNode, CriteriaHierarchy


class TestTreeNode(unittest.TestCase):
    def test_parent_value(self):
        parent = TreeNode('parent', None)
        other_parent = TreeNode('other_parent', None)
        node = TreeNode("node", parent)
        self.assertEqual(parent, node.get_parent())
        node.change_parent(other_parent)
        self.assertEqual(other_parent, node.get_parent())

    def test_children(self):
        parent = TreeNode('parent', None)
        child_one = TreeNode('one', parent)
        child_two = TreeNode('two', parent)
        parent.add_children(child_one)
        parent.add_children(child_two)
        print(parent.get_children())
        self.assertEqual(list(parent.get_children().values()), [child_one, child_two])


if __name__ == '__main__':
    unittest.main()