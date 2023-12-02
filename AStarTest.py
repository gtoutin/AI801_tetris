from A_star import AStarTetrisSolver
import copy
import tetronimoes
from UCT import CollisionDetection

class MicroState:
    movement = [['NOOP'], ['A'], ['B'], ['right'], ['right', 'A'], ['right', 'B'], ['left'], ['left', 'A'], ['left', 'B'], ['down'], ['down', 'A'], ['down', 'B']]
    SpeedtoFallFrames = [48, 43, 38, 28, 23, 18, 13, 8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    rot2num = {"v": 0, "h": 1, "u": 0, "r": 1, "d": 2, "l": 3}
    
    def __init__(self, boardstate, currentpiece, piecelocation, goalstate=None, speed=0, previousaction="NOOP", parent=None, g=0):
        self.boardstate = boardstate
        self.currentpiece = currentpiece
        self.piecelocation = list(piecelocation)
        self.goalstate = goalstate
        self.speed = speed
        self.fallframes = self.SpeedtoFallFrames[min(speed, 29)] - 1
        self.softdrop = 0
        self.previousaction = previousaction
        self.parent = parent
        self.g_score = g
        self.h_score = self.heuristic(goalstate)
        self.f_score = self.g_score + self.h_score
    
    def takeAction(self, action):
        bs = copy.deepcopy(self.boardstate)
        cp = copy.deepcopy(self.currentpiece)
        #pl = copy.deepcopy(self.piecelocation)
        
        ff = copy.deepcopy(self.fallframes)
        sd = copy.deepcopy(self.softdrop)
        
        
        
        if "A" in action and "A" not in self.previousaction:
            if cp[0] != "O":
                if cp[1] == "h":
                    cp = cp[0] + "v"
                elif cp[1] == "v":
                    cp = cp[0] + "h"
                elif cp[1] == "u":
                    cp = cp[0] + "r"
                elif cp[1] == "r":
                    cp = cp[0] + "d"
                elif cp[1] == "d":
                    cp = cp[0] + "l"
                elif cp[1] == "l":
                    cp = cp[0] + "u"
        
        if "B" in action and "B" not in self.previousaction:
            if cp[0] != "O":
                if cp[1] == "h":
                    cp = cp[0] + "v"
                elif cp[1] == "v":
                    cp = cp[0] + "h"
                elif cp[1] == "u":
                    cp = cp[0] + "l"
                elif cp[1] == "l":
                    cp = cp[0] + "d"
                elif cp[1] == "d":
                    cp = cp[0] + "r"
                elif cp[1] == "r":
                    cp = cp[0] + "u"
        
        
        
        pl = [tetronimoes.TETRO_TRANS[cp][0] + self.piecelocation[0], tetronimoes.TETRO_TRANS[cp][1] + self.piecelocation[1]]
        
        if "down" in action:
            if sd == 2 and ff > 1:
                pl[1] += 1
                sd = 1
            elif sd == 0 or sd == 1:
                sd += 1
        else:
            sd = 0
            
        
        if "left" in action and "left" not in self.previousaction:
            pl[0] -= 1
            if not CollisionDetection(bs, self.currentpiece, pl):
                pl[0] += 1
        if "right" in action and "right" not in self.previousaction:
            pl[0] += 1
            if not CollisionDetection(bs, self.currentpiece, pl):
                pl[0] -= 1
        
        pl = (pl[0] - tetronimoes.TETRO_TRANS[cp][0], pl[1] - tetronimoes.TETRO_TRANS[cp][1])
        
        
        
        ff -= 1
        if ff <= 0:
            pl[1] += 1
        #print(bs, cp, pl, self.goalstate, self.speed, action, copy.deepcopy(self), self.g_score + 1)
        
        m = MicroState(bs, cp, pl, copy.deepcopy(self.goalstate), copy.deepcopy(self.speed), action, copy.deepcopy(self), copy.deepcopy(self.g_score) + 1)
        #print(m)
        #print(self)
        m.fallframes = ff
        m.softdrop = sd
        return m
    
    def heuristic(self, goal):
        if goal is None:
            return 0
        if len(self.currentpiece) == 1:
            currot = 0
        else:
            currot = self.rot2num[self.currentpiece[1]]
        
        if len(goal.currentpiece) == 1:
            goalrot = 0
        else:
            goalrot = self.rot2num[goal.currentpiece[1]]
        rotcost = min(abs(currot - goalrot), abs(((currot + 1) % 4) - ((goalrot + 1) % 4)))
        movcostx = 2 * abs(self.piecelocation[0] - goal.piecelocation[0])
        
        #Since you can't move left/right twice consecutively, this rule has to be added to properly convey the rules
        if not ((self.piecelocation[0] - goal.piecelocation[0] < 0 and "left" in self.previousaction) or (self.piecelocation[0] - goal.piecelocation[0] > 0 and "right" in self.previousaction)):
            movcostx = max(0, movcostx - 1)
            
        movcosty = (2 * abs(self.piecelocation[1] - goal.piecelocation[1])) 
        if movcosty > 0:
            movcosty -= (self.softdrop - 1)
        movcost = movcostx + movcosty
        if goal.piecelocation[1] < self.piecelocation[1]:
            #If goal is above the current piece, it's impossible to reach and should therefore not be added
            movcost = 9999
        return rotcost + movcost
    
    def is_goal(self, goal):
        return (self.currentpiece == goal.currentpiece and self.piecelocation == goal.piecelocation)
    
    def generate_neighbors(self):
        return tuple([self.takeAction(action) for action in self.movement])
    
    def __eq__(self,other):
        #print(other)
        try:
            if self.currentpiece == other.currentpiece and tuple(self.piecelocation) == tuple(other.piecelocation) and tuple(self.previousaction) == tuple(other.previousaction) and self.softdrop == other.softdrop:
                return True
            return False
        except:
            if self.currentpiece == other[0] and tuple(self.piecelocation) == tuple(other[1]) and tuple(self.previousaction) == tuple(other[2]) and self.softdrop == other[3]:
                return True
            return False
        
    
    def __lt__(self,other):
        if self.f_score < other.f_score:
            return True
        if self.f_score == other.f_score:
            if self.h_score < other.h_score:
                return True
        return False
    
    def __gt__(self,other):
        if self.f_score > other.f_score:
            return True
        if self.f_score == other.f_score:
            if self.h_score > other.h_score:
                return True
        return False
    
    def __str__(self):
        return str([self.currentpiece, self.piecelocation, self.previousaction, self.f_score, self.h_score])
    
    def __hash__(self):
        #print(self.currentpiece)
        #print(self.piecelocation)
        #print(self.previousaction)
        return hash((self.currentpiece, tuple(self.piecelocation), tuple(self.previousaction), self.softdrop))


AStarBoard = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
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
(0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
(0, 0, 0, 0, 1, 1, 1, 0, 0, 0),
(0, 0, 0, 0, 0, 1, 1, 0, 0, 0),
(0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
(0, 0, 0, 1, 1, 1, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 1, 0, 0, 0, 0))


AGoalState = MicroState(AStarBoard, "Sv", (6, 18))
AStartState = MicroState(AStarBoard, "Sh", (5, 0), AGoalState)

AStar = AStarTetrisSolver(AStartState, AGoalState)
solved = AStar.solve()

print(solved)














