import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

V = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
G.add_nodes_from(V)

E = [
    ('S', 'A'), ('S', 'B'), ('S', 'C'),
    ('A', 'D'), ('A', 'B'),
    ('B', 'D'), ('B', 'F'), ('B', 'G'),
    ('C', 'B'), ('C', 'F'),
    ('D', 'E'),
    ('F', 'E'), ('F', 'H'),
    ('E', 'G'),
    ('H', 'G')
]
G.add_edges_from(E)

# G = nx.Graph()
# V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
# E = [
#     ('A', 'B'), ('A', 'C'),
#     ('B', 'D'), ('B', 'E'),
#     ('C', 'F'), ('C', 'G'),
#     ('D', 'H'), ('D', 'I'),
#     ('E', 'J'), ('E', 'K'),
#     ('F', 'L'), ('F', 'M'),
#     ('G', 'N'), ('G', 'O'),
# ]
# G.add_nodes_from(V)
# G.add_edges_from(E)


def BFS(initialState, goalTest):
    frontier = []
    explored = []

    frontier.append(initialState)

    while len(frontier) > 0:
        state = frontier.pop(0)
        explored.append(state)
        if goalTest == state:
            return explored
        for neighbor in G.neighbors(state):
            if neighbor not in list(set(frontier + explored)):
                frontier.append(neighbor)
    return False


def DFS(initialState, goalTest):
    frontier = []
    explored = []

    frontier.append(initialState)

    while len(frontier) > 0:
        state = frontier.pop()
        explored.append(state)
        if goalTest == state:
            return explored
        for neighbor in G.neighbors(state):
            if neighbor not in list(set(frontier + explored)):
                frontier.append(neighbor)
    return False


if __name__ == "__main__":
    result = BFS('S', 'G')
    print("")
    if result:
        s = 'phat hien: '
        for i in result:
            s += i + ' '
            print(s)
    else:
        print('Khong tim thay duong di')

    result = DFS('S', 'G')
    print("")
    if result:
        s = 'phat hien: '
        for i in result:
            s += i + ' '
            print(s)
    else:
        print('Khong tim thay duong di')
