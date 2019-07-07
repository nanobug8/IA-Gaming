class piece():

    def __init__(self, team, type, health, position):
        self.team = team
        self.type = type
        self.health = health
        self.position = position

class motion():

    def __init__(self,  piece, final_position):
        self.piece = piece
        self.final_position = final_position
        
class attack():
    
    def __init__(self, damaged, dmg_points):
        self.damaged=[]
        if not(damaged is None):
            self.damaged.append(damaged)
        if dmg_points is None:
            self.dmg_points=0
        else:
            self.dmg_points=dmg_points

class move():
    
    def __init__(self, motion, attack):
        self.motion = motion
        self.attack = attack
        
