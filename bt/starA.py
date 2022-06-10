import heapq


class Node:
    def __init__(self, name, goalCost):
        self.name = name
        self.goalCost = goalCost
        self.saveCost = None
        self.parent = None
        self.cost = 10000
        self.children = []

    def addChildren(self, list):
        for c in list:
            self.children.append(c)

    def addChild(self, Node):
        self.children.append(Node)

    def removeChild(self, name):
        for c in self.children:
            if c[0].name == name:
                self.children.remove(c)

    def getChild(self, name):
        for c in self.children:
            if c[0].name == name:
                return c
        return None

    def __eq__(self, other: object) -> bool:
        return self.name == other.name

    def __lt__(self, other: object) -> bool:
        return self.cost + self.goalCost < other.cost + other.goalCost

    def __gt__(self, other: object) -> bool:
        return self.cost + self.goalCost > other.cost + other.goalCost


class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_nodes(self, data):
        for node in data:
            self.nodes.append(node)

    def add_node(self, node):
        self.nodes.append(node)

    def add_edges(self, edges):
        for edge in edges:
            self.edges.append(edge)

    def getEdge(self, prev_node, current_node):
        for edge in self.edges:
            if edge[0] == prev_node.name and edge[1] == current_node.name:
                return edge
        return None

    def updateChildren(self):
        for node in self.nodes:
            for edge in self.edges:
                if edge[0] == node.name:
                    node.children.append(self.getNode(edge[1]))

    def getNode(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None


def update_cost(tree, current_node, prev_node):
    if tree.getEdge(prev_node, current_node) is not None:
        if (
            current_node.cost
            > prev_node.cost
            + prev_node.goalCost
            + tree.getEdge(prev_node, current_node)[2]
        ):
            current_node.cost = (
                prev_node.cost
                + prev_node.goalCost
                + tree.getEdge(prev_node, current_node)[2]
            )


def A_Star(tree, start, end):
    frontier = [start]
    heapq.heapify(frontier)
    explored = []
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)

        if state == end:
            return explored

        for child in state.children:
            update_cost(tree, child, state)
            child.parent = state
            if child.name not in list(set(node.name for node in frontier + explored)):
                heapq.heappush(frontier, child)
    return False


if __name__ == "__main__":
    tree = Tree()
    tree.add_nodes(
        [
            Node("S", 10),
            Node("A", 9),
            Node("B", 8),
            Node("C", 7),
            Node("D", 6),
            Node("E", 5),
            Node("F", 4),
            Node("G", 10),
            Node("H", 10),
            Node("K", 3),
            Node("M", 8),
            Node("N", 10),
            Node("I", 6),
            Node("J", 9),
            Node("L", 0),
            Node("Z", 0),
        ]
    )

    tree.add_edges(
        [
            ("S", "A", 5),
            ("S", "B", 6),
            ("S", "C", 5),
            ("A", "D", 5),
            ("A", "E", 7),
            ("B", "F", 3),
            ("B", "G", 4),
            ("C", "H", 10),
            ("C", "K", 4),
            ("D", "M", 5),
            ("D", "N", 10),
            ("E", "I", 8),
            ("F", "J", 4),
            ("F", "L", 4),
            ("K", "Z", 4),
        ]
    )

    tree.nodes[0].cost = 0

    tree.updateChildren()

    result = A_Star(tree, tree.nodes[0], tree.nodes[14])

    # if result:
    #     rs = []
    #     while result.parent is not None:
    #         rs.append(result.name)
    #         result = result.parent
    #     rs.append(result.name)
    #     rs.reverse()

    #     print("Explored: ")
    #     for node in rs:
    #         print(node)
    # else:
    #     print("404 Not Found!")

    if result:
        s = 'explored: '
        for i in result:
            s += str(i.name) + '\t'
            print(s)
    else:
        print('Not Found!!')
