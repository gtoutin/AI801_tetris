def CY(var):
    return max(var,0)

#Used to check collision for pieces            
#True = No problem, False = piece is inside blocks
def CollisionDetection(boardstate, currentpiece, piecelocation):
    x = int(piecelocation[0])
    y = int(piecelocation[1])
    print(x,y)
    print(x-1)
    print(boardstate[11][-1])
    try:
        if currentpiece == "O":
            if boardstate[y][x] == 0 and boardstate[CY(y+1)][x] == 0 and boardstate[CY(y)][x-1] == 0 and boardstate[CY(y+1)][x-1] == 0:
                return True
            else:
                #print(boardstate[y][x], boardstate[CY(y+1)][x], boardstate[CY(y)][x-1], boardstate[CY(y+1)][x-1])
                return False
        elif currentpiece == "Ju":
            if boardstate[y][x] == 0 and boardstate[CY(y)][x+1] == 0 and boardstate[CY(y)][x-1] == 0 and boardstate[CY(y-1)][x-1] == 0:
                return True
            else:
                #print(boardstate[y][x], boardstate[CY(y)][x+1], boardstate[CY(y)][x-1], boardstate[CY(y-1)][x-1])
                return False
        elif currentpiece == "Jd":
            if boardstate[y][x] == 0 and boardstate[CY(y)][x-1] == 0 and boardstate[CY(y)][x+1] == 0 and boardstate[CY(y+1)][x+1] == 0:
                return True
            else:
                #print(boardstate[y][x], boardstate[CY(y)][x-1], boardstate[CY(y)][x+1], boardstate[CY(y+1)][x+1])
                return False
        elif currentpiece == "Jl":
            if boardstate[y][x] == 0 and boardstate[CY(y-1)][x] == 0 and boardstate[CY(y+1)][x] == 0 and boardstate[CY(y+1)][x-1] == 0:
                return True
            else:
                #print(boardstate[y][x], boardstate[CY(y-1)][x], boardstate[CY(y+1)][x], boardstate[CY(y+1)][x-1])
                return False
        elif currentpiece == "Jr":
            if boardstate[y][x] == 0 and boardstate[CY(y+1)][x] == 0 and boardstate[CY(y-1)][x] == 0 and boardstate[CY(y-1)][x+1] == 0:
                return True
            else:
                #print(boardstate[y][x], boardstate[CY(y+1)][x], boardstate[CY(y-1)][x], boardstate[CY(y-1)][x+1])
                return False
        elif currentpiece == "Zh":
            if boardstate[y][x] == 0 and boardstate[CY(y)][x-1] == 0 and boardstate[CY(y+1)][x] == 0 and boardstate[CY(y+1)][x+1] == 0:
                return True
            else:
                return False
        elif currentpiece == "Zv":
            if boardstate[y][x] == 0 and boardstate[CY(y+1)][x] == 0 and boardstate[CY(y)][x+1] == 0 and boardstate[CY(y-1)][x+1] == 0:
                return True
            else:
                return False
        elif currentpiece == "Sh":
            if boardstate[y][x] == 0 and boardstate[CY(y)][x+1] == 0 and boardstate[CY(y+1)][x] == 0 and boardstate[CY(y+1)][x-1] == 0:
                return True
            else:
                return False
        elif currentpiece == "Sv":
            if boardstate[y][x] == 0 and boardstate[CY(y-1)][x] == 0 and boardstate[CY(y)][x+1] == 0 and boardstate[CY(y+1)][x+1] == 0:
                return True
            else:
                return False
        elif currentpiece == "Ih":
            if boardstate[y][x] == 0 and boardstate[CY(y)][x+1] == 0 and boardstate[CY(y)][x-1] == 0 and boardstate[CY(y)][x-2] == 0:
                return True
            else:
                return False
        elif currentpiece == "Iv":
            if boardstate[y][x] == 0 and boardstate[CY(y+1)][x] == 0 and boardstate[CY(y-1)][x] == 0 and boardstate[CY(y-2)][x] == 0:
                return True
            else:
                return False
        elif currentpiece == "Td":
            if boardstate[y][x] == 0 and boardstate[CY(y+1)][x] == 0 and boardstate[CY(y)][x-1] == 0 and boardstate[CY(y)][x+1] == 0:
                return True
            else:
                return False
        elif currentpiece == "Tl":
            if boardstate[y][x] == 0 and boardstate[CY(y+1)][x] == 0 and boardstate[CY(y)][x-1] == 0 and boardstate[CY(y-1)][x] == 0:
                return True
            else:
                return False
        elif currentpiece == "Tr":
            if boardstate[y][x] == 0 and boardstate[CY(y+1)][x] == 0 and boardstate[CY(y)][x+1] == 0 and boardstate[CY(y-1)][x] == 0:
                return True
            else:
                return False
        elif currentpiece == "Tu":
            if boardstate[y][x] == 0 and boardstate[CY(y-1)][x] == 0 and boardstate[CY(y)][x+1] == 0 and boardstate[CY(y)][x-1] == 0:
                return True
            else:
                return False
        elif currentpiece == "Ld":
            if boardstate[y][x] == 0 and boardstate[CY(y)][x+1] == 0 and boardstate[CY(y)][x-1] == 0 and boardstate[CY(y+1)][x-1] == 0:
                return True
            else:
                return False
        elif currentpiece == "Ll":
            if boardstate[y][x] == 0 and boardstate[CY(y+1)][x] == 0 and boardstate[CY(y-1)][x] == 0 and boardstate[CY(y-1)][x-1] == 0:
                return True
            else:
                return False
        elif currentpiece == "Lr":
            if boardstate[y][x] == 0 and boardstate[CY(y-1)][x] == 0 and boardstate[CY(y+1)][x] == 0 and boardstate[CY(y+1)][x+1] == 0:
                return True
            else:
                return False
        elif currentpiece == "Lu":
            if boardstate[y][x] == 0 and boardstate[CY(y)][x-1] == 0 and boardstate[CY(y)][x+1] == 0 and boardstate[CY(y-1)][x+1] == 0:
                return True
            else:
                return False
        else:
            #Not an accepted piecetype
            return False
    except:
        #Invalid piece location
        return False
