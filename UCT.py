# get board state
# get next piece info
# generate all possible states for the rotations of the piece
# score each state
# return what the best state is

# not simply going thru all possible next states and choosing the best one.
# spawns new games after each action, counts up the scores of each game and decides which is best?


class UCTTetrisSolver:
    def __init__(self, board):
        self.board = board

    def get_adjacent_block(self, location, direction):
        '''Given a location (i,j tuple) and a direction (up, down, left, right),
        check the block in that direction and 
        return 1 if that block is occupied or out of bounds and return 0 if that block is free.
        Assumes that an occupied block on the board has a value of 1.'''
        i = location[0]
        j = location[1]
        try:
            if direction == "up":
                return self.board[i-1][j]
            elif direction == "down":
                return self.board[i+1][j]
            elif direction == "left":
                return self.board[i][j-1]
            elif direction == "right":
                return self.board[i][j+1]
            else:
                raise ValueError("direction is not up, down, left, or right.")
        except IndexError:
            # handle out of bounds case
            # potential bug: if passing in a location that is already way out of bounds
            #  it will not tell you that you did that
            if direction == "up":
                # ceiling should not be counted as a wall
                return 0
            return 1
    
    def num_completed_rows():
        '''Return number of rows that are completed'''
        num_completed = 0
        for row in self.board:
            num_completed += all(row)
        return num_completed
    
    def num_holes():
        '''Return number of holes in the board'''
        num_holes = 0
        for i, row in self.state[0]:
            for j, block in row:
                # solid blocks aren't holes
                if board[i,j] == 1:
                    continue
                # test every direction around the current empty block. if all are solid blocks/walls, then this is a hole
                is_hole = all([self.get_adjacent_block((i,j), direction for direction in ["up", "down", "left", "right"]])
                num_holes += is_hole
        return num_holes
    
    def score_state(self):
        '''Calculate the utility of a given state.'''