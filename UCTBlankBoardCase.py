from UCT import CollisionDetection, UCTTetrisSolver
import tetronimoes

board =   ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

x = 7
y = 19
piece = "Jr"

print((tetronimoes.TETRO_TRANS[piece][0] + x, tetronimoes.TETRO_TRANS[piece][1] + y))

print(CollisionDetection(board, piece, (tetronimoes.TETRO_TRANS[piece][0] + x, tetronimoes.TETRO_TRANS[piece][1] + y)))
