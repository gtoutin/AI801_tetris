import heapq
import copy

"""
TetrisGameState.get_initial_node(): Create and return the initial game state node.
TetrisGameState.is_goal(node): Check if the node represents a goal state.
TetrisGameState.calculate_move_cost(from_node, to_node): Calculate the cost of making a move from 'from_node' to 'to_node'.
TetrisGameState.calculate_heuristic(node): Calculate the heuristic value for the given node.
TetrisNode.generate_neighbors(): Generate neighboring nodes based on valid moves.
These methods and functions will depend on the specific rules and representation of your Tetris game.
"""

# Class representing the game state of Tetris
class TetrisGameState:
    def __init__(self, board):
        self.board = board  # The game board

    def is_goal(self, node):
        # Check if the node represents a goal state
        pass

    def calculate_move_cost(self, from_node, to_node):
        # Calculate the cost of making a move from 'from_node' to 'to_node'
        pass

    def calculate_heuristic(self, node):
        # Calculate the heuristic value for the given node
        pass

# Class representing a node in the search space of Tetris
class TetrisNode:
    def __init__(self, state, position, rotation):
        self.state = state  # The game state at this node
        self.position = position  # Current position of the Tetris piece
        self.rotation = rotation  # Current rotation of the Tetris piece
        self.g_score = 0  # Cost from the start node to this node
        self.f_score = 0  # Total estimated cost of the path through this node
        self.parent = None  # Parent node in the search tree

    def generate_neighbors(self):
        # Generate neighboring nodes based on valid moves
        pass

# Class to solve Tetris using the A* algorithm
class AStarTetrisSolver:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state  # The game state representation
        self.goal_node = goal_state
        self.open_set = []  # Priority queue for open set of nodes
        self.closed_set = set()  # Set to store visited nodes
        self.path = []  # Path representing the solution

    def solve(self):
        start_node = copy.deepcopy(self.start_state)
        
        heapq.heappush(self.open_set, (0, start_node))

        while self.open_set:
            current_cost, current_node = heapq.heappop(self.open_set)
            #print(current_node)

            if current_node.is_goal(self.goal_node):
                #print(current_node.parent)
                path = self.reconstruct_path(current_node)
                #print(path)
                return path
                

            self.closed_set.add(current_node)

            for neighbor_node in current_node.generate_neighbors():
                if neighbor_node in self.closed_set or neighbor_node.f_score >= 9999:
                    continue

                tentative_g_score = current_node.g_score + 1 #self.game_state.calculate_move_cost(current_node, neighbor_node)

                if neighbor_node not in self.open_set or tentative_g_score < neighbor_node.g_score:
                    neighbor_node.g_score = tentative_g_score
                    neighbor_node.f_score = tentative_g_score + neighbor_node.heuristic(self.goal_node)
                    neighbor_node.parent = current_node

                    if neighbor_node not in self.open_set:
                        heapq.heappush(self.open_set, (neighbor_node.f_score, neighbor_node))

        return None

    def reconstruct_path(self, node):
        #print(node)
        #print(node.parent)
        #print(node.previousaction)
        #print(node.softdrop)
        path = []
        locpath = []
        cppath = []
        path.append(['NOOP'])
        locpath.append(node.piecelocation)
        for i in range(0, 3 - node.softdrop):
            path.append(['down'])
            locpath.append(node.piecelocation)
            cppath.append(node.currentpiece)
        while node.parent is not None:
            path.append(node.previousaction)
            node = node.parent
            locpath.append(node.piecelocation)
            cppath.append(node.currentpiece)
            #print(path)
        #print(path)
        path.reverse()
        locpath.reverse()
        cppath.reverse()
        return (path, locpath, cppath)

    
