# get board state
# get next piece info
# generate all possible states for the rotations of the piece
# score each state
# return what the best state is

# not simply going thru all possible next states and choosing the best one.
# spawns new games after each action, counts up the scores of each game and decides which is best?

import random
import Tetris, tetronimoes


global PIECES
PIECES = ['O', 'Zh', 'Zv', 'Sh', 'Sv', 'Ih', 'Iv']
for piece in ['J', 'T', 'L']:
    for direction in ['u', 'd', 'l', 'r']:
        PIECES.append(piece+direction)
global BOARD_WIDTH
BOARD_WIDTH = 10
global BOARD_HEIGHT
BOARD_HEIGHT = 20

random.seed(1)

def get_rotations(piece):
    '''Given a piece, return list of pieces that it will become when rotated'''
    if piece[0] == "O":
        return ["O"]
    if piece[0] in ["Z", "S", "I"]:
        return [piece[0]+rot for rot in ['h','v']]
    if piece[0] in ['J', 'T', 'L']:
        return [piece[0]+rot for rot in ['u', 'd', 'l', 'r']]


class UCTTetrisSolver:
    def __init__(self, board):
        # current board. copy this when doing calculations instead of modifying this copy
        self.board = board

    def get_adjacent_block(self, board, location, direction):
        '''Given a location (i,j tuple) and a direction (up, down, left, right),
        check the block in that direction and 
        return 1 if that block is occupied or out of bounds and return 0 if that block is free.
        Assumes that an occupied block on the board has a value of 1.'''
        i = location[0]
        j = location[1]
        try:
            if direction == "up":
                return board[i-1][j]
            elif direction == "down":
                return board[i+1][j]
            elif direction == "left":
                return board[i][j-1]
            elif direction == "right":
                return board[i][j+1]
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
    
    def num_completed_rows(self, board):
        '''Return number of rows that are completed'''
        num_completed = 0
        for row in board:
            num_completed += all(row)
        return num_completed
    
    def num_holes(self, board):
        '''Return number of holes in the board'''
        num_holes = 0
        for i, row in enumerate(board):
            for j, block in enumerate(row):
                # solid blocks aren't holes
                if block == 1:
                    continue
                # test every direction around the current empty block. if all are solid blocks/walls, then this is a hole
                is_hole = all([self.get_adjacent_block(board, (i,j), direction) for direction in ["up", "down", "left", "right"]])
                num_holes += is_hole
        return num_holes

    def block_height(self, board):
        '''Return height of blocks placed on board. Higher number is worse'''
        for i, row in enumerate(board):
            if 1 in row:
                return BOARD_HEIGHT - i

    def score_state(self, board):
        '''Calculate the utility of a given state.'''
        # number of wells is bad bc they can only be removed w i piece
        # height of cols
        # diff in height of cols on board
        return self.num_completed_rows(board) - 2 * self.num_holes(board) - self.block_height(board)
        
    def place_piece(self, piece, board, location):
        '''Return a board with the piece placed at the specified location.'''
        # fetch 4x4 mask
        mask = tetronimoes.TETRO_MASKS[piece]
        # overlay mask on board at location
        # check for any errors
        for row in range(4):
            for col in range(4):
                try:
                    # ASSUMING piece is placed in empty location
                    trans_rowcol = tetronimoes.conv_xy_rowcol(tetronimoes.TETRO_TRANS[piece])
                    # it's -trans_rowcol because we are moving the board, not the piece
                    board[location+row-trans_rowcol[0]][location+col-trans_rowcol[1]] += mask[row][col]
                finally:
                    print("something is wrong, tried to place piece hanging off the board")
                    continue
        # return that board
        return board

    def drop_piece(self, piece, board, y):
        '''Drops a piece into the board at the specified horizontal (y) location'''
        # overhang issue? ignoring for now since it isn't strictly necessary
        # down is x+1, right is y+1
        location = (0,y)
        for x in range(BOARD_HEIGHT):
            if Tetris.CollisionDetection(board, piece, (x, y)):
                break
            else:
                # save board state so it will be accurate when collision is detected
                board = self.place_piece(piece, board, (x,y))
        return board, location

    def run_sim(self, board):
        '''Run a sim. 5 pieces ahead. The state passed in has the current 
        piece already placed, so start with the next piece.'''
        # get next piece
        # get 3 more random pieces
        pieces = [self.state.next_piece]
        # randomly rotate next too?
        for i in range(3):
            pieces.append(random.choice(PIECES))

        # for each piece, drop them in random places
        board = self.drop_piece(piece, board, random.randint(0,BOARD_WIDTH-1))
        # return the score
        return self.score_state(board)

    def run(self, curr_piece, curr_board):
        '''Returns piece and location of highest score'''
        # NOTE: what would be best? board state mapped to score or (piece, location x,y) mapped to score?

        best_move = {
            "piece": curr_piece,
            "location": (-1, -1),
            "score": -1000
        }
        # call run_sim for each possible placement/rotation of the current piece
        # get rotations of current piece
        for piece in get_rotations(curr_piece):
            # for each horizontal location it can be dropped in
            # ASSUMING the dropping function will take care of invalid input
            for y in range(BOARD_WIDTH):
                # drop the piece in
                board, location = self.drop_piece(piece, curr_board, y)
                # run one or 10 or whatever number of sims
                scores = [self.run_sim(board) for _ in range(10)]
                # average the scores
                avg_score = sum(scores)/len(scores)
                # if this score is better than current score, store this move
                if avg_score > best_move['score']:
                    best_move = {
                        "piece": piece,
                        "location": location,
                        "score": avg_score
                    }
        # return ALL possible moves ranked by score if A* says not possible
        # brute force each of the 5 pieces and then score
        # use formula
        return best_move

# generate all possible end states for a given piece
# for each state, run 10 sims throwing next piece and 3 more random pieces in random spots
# for each state, find the mean score
# choose the state with the highest score as the best spot