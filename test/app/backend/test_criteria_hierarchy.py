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

    def test_simple_hierarchy(self):
        hierarchy = CriteriaHierarchy()
        true_criteria_list = ['price', 'size', 'transportation', 'neighborhood', 'house age', 'yard space',
                              'facilities', 'general conditions']
        for criterion in true_criteria_list:
            hierarchy.add_node(criterion, parent_name="Result", children_names=[])
        hierarchy.criteria_list()

        all_criteria = true_criteria_list[:]
        all_criteria.append("Result")
        self.assertEqual(set(all_criteria), set(hierarchy.criteria_list()))

        criterion_levels = hierarchy.get_criterion_levels()
        self.assertEqual(set(criterion_levels.keys()), {0, 1})
        self.assertEqual(len(criterion_levels[0]), 1)
        self.assertEqual(len(criterion_levels[1]), len(true_criteria_list))
        self.assertEqual(len(hierarchy.node_dict['Result'].get_children()), len(true_criteria_list))

    def test_complex_hierarchy(self):
        hierarchy = CriteriaHierarchy()
        cost_subcriteria = ['purchase price', 'fuel cost', 'maintenance cost']
        capacity_subcriteria = ['trunk size', 'passenger capacity']
        criteria = ['cost', 'capacity', 'safety', 'design', 'warranty']

        for sub_criterion in cost_subcriteria:
            hierarchy.add_node(sub_criterion, parent_name="Result", children_names=[])
        for sub_criterion in capacity_subcriteria:
            hierarchy.add_node(sub_criterion, parent_name="Result", children_names=[])
        hierarchy.add_node(criteria[0], parent_name="Result", children_names=cost_subcriteria)
        hierarchy.add_node(criteria[1], parent_name="Result", children_names=capacity_subcriteria)
        for criterion in criteria[2:]:
            hierarchy.add_node(criterion, parent_name="Result", children_names=[])

        all_criteria = hierarchy.criteria_list()
        all_criteria_true = set(criteria).union(capacity_subcriteria).union(cost_subcriteria).union({'Result'})
        self.assertEqual(set(all_criteria), all_criteria_true)

        criterion_levels = hierarchy.get_criterion_levels()
        self.assertEqual(set(criterion_levels.keys()), {0, 1, 2})
        self.assertEqual(len(criterion_levels[0]), 1)
        self.assertEqual(len(criterion_levels[1]), len(criteria))
        self.assertEqual(len(criterion_levels[2]), len(capacity_subcriteria) + len(cost_subcriteria))
        self.assertEqual(hierarchy.node_dict['fuel cost'].get_parent(), hierarchy.node_dict["cost"])



if __name__ == '__main__':
    unittest.main()