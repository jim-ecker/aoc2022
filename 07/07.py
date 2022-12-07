from collections import defaultdict
import re


class TreeNode:  # represents a directory or file
    def __init__(self, name):
        """
        Create a new node
        :param name:    Name of the node
        """
        self.name = name
        self.children = None
        self.parent = None
        self.size = 0

    def insert(self, child: str, size: int = None) -> 'TreeNode':
        """
        Insert a child node into the tree
        :param child:   Name of the child node
        :param size:    Size of the child node
        :return:    The child node
        """
        if self.children is None:
            self.children = defaultdict(TreeNode)
        self.children[child] = TreeNode(child)
        if size is not None:
            self.children[child].size = size
            self.size += size
            node = self
            while node.parent is not None:
                node.parent.size += size
                node = node.parent
        self.children[child].parent = self
        return self.children[child]


def build_tree(root: TreeNode, lines: list) -> TreeNode:
    """
    Build a tree from a list of lines
    :param root:    Root node
    :param lines:   List of lines
    :return:    Root node
    """
    here = root
    for entry in lines:
        if re.search(r'^\$ cd (\w+)', entry):
            match = re.search(r'^\$ cd (\w+)', entry)
            directory = match.group(1)
            here = here.children[directory]
        elif re.search(r'^\$ cd \.\.', entry):
            here = here.parent
        elif re.search(r'^$ cd \/', entry):
            here = root
        elif re.search(r'^dir', entry):
            match = re.search(r'^dir (\w+)', entry)
            directory = match.group(1)
            here.insert(directory)
        elif re.search(r'^([0-9]+) (\w+\.*\w*)', entry):
            match = re.search(r'^([0-9]+) (\w+\.*\w*)', entry)
            here.insert(match.group(2), int(match.group(1)))
    return root


def get_sizes(root: TreeNode) -> list:
    """
    Get the sizes of all the directories
    :param root:    Root node
    :return:    List of sizes
    """
    sizes = []
    stack = [root]
    while stack:
        node = stack.pop()
        sizes.append(node)
        if node.children:
            for child in node.children.values():
                stack.append(child)
    return sizes


def filter_directories_by_size(root: TreeNode, N: int, gt: bool = False) -> list:
    """
    Filter directories by size
    :param root:    Root node
    :param N:   Size to filter by
    :param gt:  Whether to filter by greater than or less than
    :return:    List of directories
    """
    directories = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node.children:
            if not gt:
                if node.size <= N:
                    directories.append(node)
            else:
                if node.size >= N:
                    directories.append(node)
            for child in node.children.values():
                stack.append(child)
    return directories


d = []
with open("input.txt") as f:
    for line in f.read().split('\n'):
        d.append(line)

root = TreeNode('/')
root = build_tree(root, d[1:])

print('part 1: {}'.format(sum([node.size for node in filter_directories_by_size(root, 100000)])))
print('part 2: {}'.format(min([node.size for node in filter_directories_by_size(root, 30000000 - (70000000 - root.size), gt=True)])))
