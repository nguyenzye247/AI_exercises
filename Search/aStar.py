import heapq
from TreeNode import *


def update_cost(tree, current_node, prev_node):
    if tree.get_edge(prev_node, current_node) is not None:
        if current_node.cost > prev_node.cost + tree.get_edge(prev_node, current_node)[2]:
            current_node.cost = prev_node.cost + \
                tree.get_edge(prev_node, current_node)[2]


def A_Star(tree, start, end):
    frontier = [start]
    explored = []
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        print(state)
        if state == end:
            return explored
        for child in state.neighbors():
            update_cost(tree, child, state)
            if child.get_label() not in list(set(node.get_label() for node in frontier + explored)):
                heapq.heappush(frontier, child)
    return False


if __name__ == "__main__":
    tree = Tree()
    tree.add_nodes(
        [
            Node("A", 6),
            Node("B", 3),
            Node("C", 4),
            Node("D", 5),
            Node("E", 3),
            Node("F", 1),
            Node("G", 6),
            Node("H", 2),
            Node("I", 5),
            Node("J", 4),
            Node("K", 2),
            Node("L", 0),
            Node("M", 4),
            Node("N", 0),
            Node("O", 4)
        ]
    )

    tree.add_edges([
        ("A", "B", 2),
        ("A", "C", 1),
        ("A", "D", 3),
        ("B", "E", 5),
        ("B", "F", 4),
        ("C", "G", 6),
        ("C", "H", 3),
        ("D", "I", 2),
        ("D", "J", 4),
        ("F", "K", 2),
        ("F", "L", 1),
        ("F", "M", 4),
        ("H", "N", 2),
        ("H", "O", 4),
    ])
    tree.nodes[0].cost = 0

    print("rs")
    result = A_Star(tree, tree.nodes[0], tree.nodes[14])
    if result:
        s = 'explored: '
        for i in result:
            s += str(i.label) + ' - ' + str(i.cost) + \
                ' - ' + str(i.goal_cost) + '\t'
            print(s)
    else:
        print('Not Found!!')
