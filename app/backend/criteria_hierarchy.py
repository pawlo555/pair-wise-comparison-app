from typing import Dict, List


class CriteriaHierarchy:
    """
    Class to manage dependencies between criteria - to enable to multi layers comparison
    """
    def __init__(self):
        self.root = TreeNode("Result", None)
        self.node_dict = {"Result": self.root}

    def add_node(self, node_name: str, parent_name: str, children_names: List[str]) -> None:
        """
        Adds note do the tree, perform all operation to maintain structure of tree
        :param node_name: Name of node to add to tree
        :param parent_name: Name of node who will be parent do added nodes
        :param children_names: List of children names - if children already have a parent it will be replaced
        """
        assert node_name not in self.node_dict, "Node of name: " + node_name + " is already in use"
        parent = self.node_dict[parent_name]
        new_node = TreeNode(node_name, parent)
        parent.add_children(new_node)
        self.node_dict[node_name] = new_node
        for child_name in children_names:
            child_node = self.node_dict[child_name]
            new_node.add_children(child_node)
            child_node.change_parent(new_node)

    def remove_node(self, node_name: str) -> None:
        """
        Remove element from the tree, if there is no such element do nothing
        :param node_name: Name of node to remove
        """
        if node_name == "Result":
            return
        node_to_remove = self.node_dict[node_name]
        parent = node_to_remove.get_parent()
        parent.remove_children(node_to_remove)
        children = node_to_remove.get_children()
        for child in children.values():
            parent.add_children(child)

    def criteria_list(self) -> List[str]:
        """
        :return: Sorted listed of criteria names in hierarchy
        """
        return sorted(list(self.node_dict.keys()))

    def get_level(self, criterion_name) -> int:
        """
        Return the level of criterion in the tree, 0 is for the root, root's children have level 1 itd.
        :param criterion_name: Name of the criterion
        :return: Level of node in the tree
        """
        current_level = 0
        current_node = self.node_dict[criterion_name]
        while current_node.get_parent() is not None:
            current_level = current_level+1
            current_node = current_node.get_parent()
        return current_level

    def get_criterion_levels(self) -> Dict[int, List[str]]:
        """
        Returns a dictionary containing information about tree structure:
        for each key we have a list of criteria names with level got in key
        :return: Dictionary: level - List of criteria with this level in the tree
        """
        criteria_levels = {}
        for criterion_name in criteria_levels:
            level = self.get_level(criterion_name)
            if level not in criteria_levels.keys():
                criteria_levels[level] = [criterion_name]
            else:
                criteria_levels[level].append(criterion_name)
        return criteria_levels


class TreeNode:
    """
    Class represent single object in CriteriaHierarchy
    """
    def __init__(self, name: str, parent: 'TreeNode'):
        self.children = {}
        self.__parent = parent
        self.__name = name

    def add_children(self, child: 'TreeNode') -> None:
        self.children[child.__name] = child

    def remove_children(self, child: 'TreeNode') -> None:
        self.children.pop(child.__name)

    def get_children(self) -> Dict[str, 'TreeNode']:
        return self.children

    def get_parent(self) -> 'TreeNode':
        return self.__parent

    def change_parent(self, new_parent: 'TreeNode') -> None:
        self.__parent = new_parent
