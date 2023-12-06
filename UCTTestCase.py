from UCT import UCTTetrisSolver

UCTTestBoard =   ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
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
                  (0, 1, 0, 1, 0, 0, 1, 0, 1, 0), 
                  (0, 1, 0, 1, 0, 0, 1, 0, 1, 0), 
                  (0, 1, 0, 1, 0, 0, 1, 0, 1, 0), 
                  (0, 1, 0, 1, 0, 0, 1, 0, 1, 0), 
                  (0, 1, 0, 1, 0, 0, 1, 0, 1, 0), 
                  (1, 1, 1, 1, 0, 0, 1, 1, 1, 1), 
                  (1, 1, 1, 1, 0, 1, 1, 1, 1, 1), 
                  (1, 1, 1, 1, 0, 1, 1, 1, 1, 1))
UCTPiece = "Jl"
UCTNextPiece = "O"
UCTGoalLocation = (4,18) #Jr

class MacroState:
    
    def __init__(self, boardstate, currentpiece, nextpiece):
        self.boardstate = boardstate
        self.currentpiece = currentpiece
        self.next_piece = nextpiece

UCTTest = MacroState(UCTTestBoard, UCTPiece, UCTNextPiece)
uct = UCTTetrisSolver(UCTTestBoard, UCTTest)
print(uct.run(UCTPiece, UCTTestBoard))
