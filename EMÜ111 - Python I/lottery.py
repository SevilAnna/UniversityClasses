import random

def draw():
    p1 = random.randint(1,49)
    p2 = random.randint(1,49)
    while p1==p2:
        p2 = random.randint(1, 49)
    p3 = random.randint(1,49)
    while p1==p3 or p2==p3:
        p3 = random.randint(1, 49)
    p4 = random.randint(1,49)
    while p1==p4 or p2==p4 or p3==p4:
        p4 = random.randint(1, 49)
    p5 = random.randint(1,49)
    while p1==p5 or p2==p5 or p3==p5 or p4==p5:
        p5 = random.randint(1, 49)
    p6 = random.randint(1,49)
    while p1==p6 or p2==p6 or p3==p6 or p4==p6 or p5==p6:
        p6 = random.randint(1, 49)

    return(p1,p2,p3,p4,p5,p6)

def check_win(p1,p2,p3,p4,p5,p6):
    winner = True
    if c1 != p1 and c1 != p2 and c1 != p3 and c1 != p4 and c1 != p5 and c1 != p6:
        winner = False
    if c2 != p1 and c2 != p2 and c2 != p3 and c2 != p4 and c2 != p5 and c2 != p6:
        winner = False
    if c3 != p1 and c3 != p2 and c3 != p3 and c3 != p4 and c3 != p5 and c3 != p6:
        winner = False
    if c4 != p1 and c4 != p2 and c4 != p3 and c4 != p4 and c4 != p5 and c4 != p6:
        winner = False
    if c5 != p1 and c5 != p2 and c5 != p3 and c5 != p4 and c5 != p5 and c5 != p6:
        winner = False
    if c6 != p1 and c6 != p2 and c6 != p3 and c6 != p4 and c6 != p5 and c6 != p6:
        winner = False