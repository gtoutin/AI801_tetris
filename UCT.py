# get board state
# get next piece info
# generate all possible states for the rotations of the piece
# score each state
# return what the best state is

# not simply going thru all possible next states and choosing the best one.
# spawns new games after each action, counts up the scores of each game and decides which is best?

import random
import tetronimoes
#from CollisionDetection import CollisionDetection
import copy

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

def LocBoard(x,y):
    if 0 <= x and x < 10 and 0 <= y and y < 20:
        return True
    return False

def CollisionDetection(board, currentpiece, piecelocation):
    mask = tetronimoes.TETRO_MASKS[currentpiece]
    #Piecelocation is assumed to be the top left portion of the mask, as found by tetronimoes.TETRO_TRANS
    #It is also assumed to be in the format (x,y)
    #As such, it needs to be reversed for board purposes.
    #location = tetronimoes.conv_xy_rowcol(piecelocation)
    location = piecelocation
    if location[0] == 4:
        print(location)
    for row in range(0, 4):
        for col in range(0,4):
            x = location[0] + row
            y = location[1] + col
            #print(LocBoard(x,y), x, y)
            if (not LocBoard(x,y)) or board[y][x] >= 1:
                #print(currentpiece, piecelocation, row, col)
                if mask[col][row] >= 1:
                    return False
    return True
            
            
    

def get_rotations(piece):
    '''Given a piece, return list of pieces that it will become when rotated'''
    if piece[0] == "O":
        return ["O"]
    if piece[0] in ["Z", "S", "I"]:
        return [piece[0]+rot for rot in ['h','v']]
    if piece[0] in ['J', 'T', 'L']:
        return [piece[0]+rot for rot in ['u', 'd', 'l', 'r']]


class UCTTetrisSolver:
    def __init__(self, board, state):
        # current board. copy this when doing calculations instead of modifying this copy
        self.board = board
        # state must contain next_piece
        self.state = state

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
    
    #def num_completed_rows(self, board):
    #    '''Return number of rows that are completed'''
    #    num_completed = 0
    #    for row in board:
    #        num_completed += all(row)
    #    return num_completed
    
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
        #print(board)
        for i, row in enumerate(board):
            #print(i)
            #print(row)
            if 1 in row:
                #print(BOARD_HEIGHT)
                #print(i)
                return BOARD_HEIGHT - i

    def score_state(self, board, num_completed):
        '''Calculate the utility of a given state.'''
        # number of wells is bad bc they can only be removed w i piece
        # height of cols
        # diff in height of cols on board
        temp = (num_completed * 20) - 2 * self.num_holes(board)
        #print(temp)
        return temp - self.block_height(board)
        
    def place_piece(self, piece, board, location):
        '''Return a board with the piece placed at the specified location. Takes (x,y) location.
        Returns original board if there is an error placing the piece. Returns ok bool'''
        # save board in case placing piece fails
        old_board = copy.deepcopy(board)
        # fetch 4x4 mask
        # breakpoint()
        # mask is list of lists
        print(piece, location)
        mask = tetronimoes.TETRO_MASKS[piece]
        # overlay mask on board at location
        # check for any errors
        # convert all to (row,col) bc that's how python indexing works
        location = tetronimoes.conv_xy_rowcol(location)
        #print(location)
        #trans_rowcol = tetronimoes.conv_xy_rowcol(tetronimoes.TETRO_TRANS[piece])
        #print(trans_rowcol)
        for row in range(4):
            for col in range(4):
                try:
                    # ASSUMING piece is placed in empty location
                    # it's -trans_rowcol because we are moving the board, not the piece
                    #new_row, new_col = location[0]+row-trans_rowcol[0], location[1]+col-trans_rowcol[1]
                    new_row, new_col = location[0]+row, location[1]+col
                    #print(new_row, new_col)
                    board[new_row][new_col] += mask[row][col]
                except IndexError: #finally:
                    # breakpoint()
                    print(f"tried to place {piece} at {tetronimoes.conv_xy_rowcol((new_row, new_col))}")
                    return old_board, False
              
        print(f"placed piece {piece}")
        
        # sanity checks
        assert(board != old_board)
        # didn't overlap this piece with others
        #for row in board:
        #    print(row)
        print()
        assert(all(2 not in row for row in board))
        # return that board
        return board, True

    def drop_piece(self, piece, board, x):
        '''Drops a piece into the board at the specified horizontal (x or col) location'''
        # overhang issue? ignoring for now since it isn't strictly necessary

        # save old board in case piece cannot be placed
        old_board = copy.deepcopy(board)

        # down is y+1, right is x+1
        location = (x,19)
        ok = False
        for y in reversed(range(BOARD_HEIGHT)):
            #print(y)
            if CollisionDetection(board, piece, (tetronimoes.TETRO_TRANS[piece][0] + x, tetronimoes.TETRO_TRANS[piece][1] + y)):
                # breakpoint()
                # save board state so it will be accurate when collision is detected
                location = (x,y)
                print(tetronimoes.TETRO_TRANS[piece][0] + x, tetronimoes.TETRO_TRANS[piece][1] + y)
                board, ok = self.place_piece(piece, board, (tetronimoes.TETRO_TRANS[piece][0] + x, tetronimoes.TETRO_TRANS[piece][1] + y))
                # if error, piece cannot be placed
                if not ok:
                    return old_board, location, ok, 0
                # breakpoint()
                #print("break")
                break
        #breakpoint()        
        #print(board)
        #for row in board:
        #    print(row)
        # subtract tetro_trans value for this piece to account for center
        new_board = tuple_to_list_board(board)
        row = 0
        num_completed = 0
        while row < len(new_board):
            num_completed += all(element == 1 for element in new_board[row])
            if all(element == 1 for element in new_board[row]):
                del new_board[row]
            else:
                row += 1
        
        while len(new_board) < 20:
            new_board.insert(0,[0,0,0,0,0,0,0,0,0,0])
        
        trans_rowcol = tetronimoes.conv_xy_rowcol(tetronimoes.TETRO_TRANS[piece])
        location = tetronimoes.conv_xy_rowcol(location)
        #location = [location[0], location[1]]
        return new_board, location, ok, num_completed

    def run_sim(self, board, num_completed):
        '''Run a sim. 5 pieces ahead. The state passed in has the current 
        piece already placed, so start with the next piece.'''
        # get next piece
        pieces = [self.state.next_piece]
        # get 3 more random pieces
        for _ in range(3):
            pieces.append(random.choice(PIECES))
        
        # for each piece, drop them in random places
        for piece in pieces:
            # random choice of place won't work all the time. try again until it does
            ok = False
            while not ok:
                board, location, ok, num_c = self.drop_piece(piece, board, random.randint(0, BOARD_WIDTH-1))
            num_completed += num_c

        # return the score
        #print(board[0][0][0][0])
        # breakpoint()
        return self.score_state(board, num_completed)

    def run(self, curr_piece, curr_board):
        '''Returns piece and location of highest score'''
        curr_board = tuple_to_list_board(curr_board)

        best_move = {
            "piece": curr_piece,
            "location": (-1, -1),
            "score": -1000
        }
        num_completed = 0
        all_moves = []
        all_moves.append(best_move)
        # call run_sim for each possible placement/rotation of the current piece
        # get rotations of current piece
        #print(curr_piece)
        
        for piece in get_rotations(curr_piece):
            # for each horizontal location it can be dropped in
            # ASSUMING the dropping function will take care of invalid input
            for x in range(BOARD_WIDTH):
                # drop the piece in
                #for row in curr_board:
                #    print(row)
                board, location, ok, num_completed = self.drop_piece(piece, copy.deepcopy(curr_board), x)
                
                #for row in board:
                #    print(row)
                # breakpoint()
                # could try to drop in invalid place
                if not ok:
                    continue
                assert(board != curr_board)
                # run one or 10 or whatever number of sims
                scores = [self.run_sim(board, num_completed) for _ in range(10)]
                # average the scores
                avg_score = sum(scores)/len(scores)
                print(piece, x, avg_score, location)
                print(avg_score, best_move['score'])
                print(avg_score > best_move['score'])
                # if this score is better than current score, store this move
                if avg_score > best_move['score']:
                    best_move = {
                        "piece": piece,
                        "location": location,
                        "score": avg_score
                    }
                    all_moves.append(best_move)
                    #print(all_moves)
                    print("better move found")
                    print(x, best_move, piece, curr_piece)
        # possible for future: return ALL possible moves ranked by score if A* says not possible
        # brute force each of the 5 pieces and then score
        # use formula
        return all_moves

# generate all possible end states for a given piece
# for each state, run 10 sims throwing next piece and 3 more random pieces in random spots
# for each state, find the mean score
# choose the state with the highest score as the best spot

def tuple_to_list_board(board):
    '''Convert tuple of tuples to list of lists. Creates deep copy.'''
    b = []
    for row in board:
        b.append(list(row))
    return b