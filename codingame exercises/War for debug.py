import random
from collections import deque

cardp_1 = deque()
cardp_2 = deque()

#VALORES ALEATÓRIOS PARA TESTE
for i in range(3):
    cardp_1.append(random.randrange(13))
    cardp_2.append(random.randrange(13))
"""
cardp_1.append(50)
cardp_2.append(50)
"""
print(cardp_1)
print(cardp_2)

"""
n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1.append(input())  # the n cards of player 1
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2.append(input())  # the m cards of player 2
"""
special = False
rounds = 0

def flip(P1, P2):

    global special

    p1 = P1.popleft()
    p2 = P2.popleft()
    
    if p1 > p2:
        P1.append(p1)
        P1.append(p2)
    if p1 < p2:
        P2.append(p1)
        P2.append(p2)
    if p1 == p2:
        pp1 = deque()
        pp2 = deque()
        
        for i in range(3):
            if P1 != deque([]):
                pp1.append(P1.popleft())
            else:
                special = True
            if P2 != deque([]):
                pp2.append(P2.popleft())
            else:
                special = True
        while pp1 != deque([]) and pp2 != deque([]) and not special and rounds < 1000:
            flip(pp1, pp2)

while cardp_1 != deque([]) and cardp_2 != deque([]) and not special and rounds < 1000:
    print('\nplayer 1',cardp_1)
    print('\nplayer 2',cardp_2)
    flip(cardp_1, cardp_2)
    rounds += 1

if special:
    print('PAT')
elif cardp_1 == deque([]):
    print(2,rounds)
elif cardp_2 == deque([]):
    print(1,rounds)
print('\nplayer 1 FINAL:',cardp_1)
print('player 2 FINAL:',cardp_2)
print(rounds)