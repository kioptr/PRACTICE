from collections import deque

v = {
    '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
    '9':9,'10':10,'J':11,'Q':12,'K':13,'A':14
}

cardp_1 = deque()
cardp_2 = deque()

n = int(input())  # the number of cards for player 1
for i in range(n):
    carta_com_naipe = input()
    carta_numero = ''
    for s in carta_com_naipe:
        if s.isdigit() or s in ['J','Q','K','A']:
            carta_numero += s
    cardp_1.append(v[carta_numero])  # the n cards of player 1

m = int(input())  # the number of cards for player 2
for i in range(m):
    carta_com_naipe = input()
    carta_numero = ''
    for s in carta_com_naipe:
        if s.isdigit() or s in ['J','Q','K','A']:
            carta_numero += s
    cardp_2.append(v[carta_numero])  # the n cards of player 2

special = False
rounds = 0

def flip(P1, P2):

    global special,p1v,p2v

    p1 = P1.popleft()
    p2 = P2.popleft()
    p1_temp.append(p1)
    p2_temp.append(p2)

    if p1 > p2:
        p1v += 1
    if p1 < p2:
        p2v += 1
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

    """COLOCAR AQUI"""
    '''
    for i in p1_temp:
        P2.append(i)
    for i in p2_temp:
        P2.append(i)
    '''
    #adicionar


while cardp_1 != deque([]) and cardp_2 != deque([]) and not special and rounds < 1000:

    p1v = p2v = 0
    p1_temp = p2_temp = []
    flip(cardp_1, cardp_2)
    rounds += 1

if special:
    print('PAT')
elif cardp_1 == deque([]):
    print(2,rounds)
elif cardp_2 == deque([]):
    print(1,rounds)