import heapq


class Node:
    def __init__(self, label, goal_cost):
        self.label = label
        self.cost = 10000
        self.goal_cost = goal_cost
        self.save_cost = None
        self.pr = []
        self.chld = []

    def __repr__(self):
        return str(dict({
            "label": self.label,
            "cost": self.cost,
            "goal_cost": self.goal_cost
        }))

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        if self.save_cost == 10000:
            return self.goal_cost + self.cost < other.goal_cost + other.cost
        else:
            return self.cost < other.cost

    def get_label(self):
        return self.label

    def neighbors(self):
        return self.chld + self.pr


class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_nodes(self, data):
        for node in data:
            self.nodes.append(node)

    def add_node(self, node):
        self.nodes.append(node)

    def get_index(self, node):
        for i, n in enumerate(self.nodes):
            if n.get_label() == node.get_label():
                return i
        return -1

    def add_edges(self, tuple_edges):
        for t in tuple_edges:
            start_label = t[0]
            end_label = t[1]
            w = t[2]
            index_start_label = self.get_index(Node(start_label, None))
            index_end_label = self.get_index(Node(end_label, None))
            self.nodes[index_start_label].chld.append(
                self.nodes[index_end_label])
            self.nodes[index_end_label].pr.append(
                self.nodes[index_start_label])
            self.edges.append(
                (self.nodes[index_start_label], self.nodes[index_end_label], t[2]))

    def show_nodes(self):
        return [node.get_data() for node in self.nodes]

    def get_edge(self, start_node, end_node):
        try:
            return [edges for edges in self.edges if edges[0] == start_node
                    and edges[1] == end_node][0]
        except:
            return None
