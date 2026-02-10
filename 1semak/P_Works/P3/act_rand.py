import random as r

def player():
    actor = r.randint(1, 2)
    if actor == 1:
        actor_1 = True
    else:
        actor_1 = False
    return actor_1