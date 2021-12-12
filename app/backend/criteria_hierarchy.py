from typing import Dict, List


class CriteriaHierarchy:
    """
    Class to manage dependencies between criteria - to enable to multi layers comparison
    """
    def __init__(self):
        self.root = TreeNode("Result", None)
        self.node_dict = {"Result": self.root}

    def add_node(self, node_name: str, parent_name: str, children_names: List[str]) -> None:
        assert node_name not in self.node_dict, "Node of name: " + node_name + " is already in use"
        parent = self.node_dict[parent_name]
        new_node = TreeNode(node_name, parent)
        parent.add_children(new_node)
        self.node_dict[node_name] = new_node
        for child_name in children_names:
            child_node = self.node_dict[child_name]
            new_node.add_children(child_node)
            child_node.change_parent(new_node)

    def remove_node(self, node_name: str):
        if node_name == "Result":
            return
        node_to_remove = self.node_dict[node_name]
        parent = node_to_remove.get_parent()
        parent.remove_children(node_to_remove)
        children = node_to_remove.get_children()
        for child in children.values():
            parent.add_children(child)

    def criteria_list(self) -> List[str]:
        return sorted(list(self.node_dict.keys()))


class TreeNode:
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
