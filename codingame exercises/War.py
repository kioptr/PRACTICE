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

print(cardp_1)
print(cardp_2)

special = False
rounds = 0

def war(P1,P2,p1,p2):

    global special

    P1_temp = []
    P2_temp = []
    p1v = p2v = 0

    P1_temp.append(p1)
    P2_temp.append(p2)

    if p1 > p2:
        p1v += 1
    if p1 < p2:
        p2v += 1
    if p1 == p2:
        PP1 = deque()
        PP2 = deque()

        for i in range(3):
            if P1 != deque([]):
                PP1.append(P1.popleft())
            else:
                special = True
            if P2 != deque([]):
                PP2.append(P2.popleft())
            else:
                special = True
        while PP1 != deque([]) and PP2 != deque([]) and not special and rounds < 1000:
            P1 = PP1.popleft()
            P2 = PP2.popleft()
            war(PP1, PP2, P1, P2)

    if p1v > p2v:
        for i in P1_temp:
            P1.append(i)
        for i in P2_temp:
            P1.append(i)
    if p1v < p2v:
        for i in P1_temp:
            P2.append(i)
        for i in P2_temp:
            P2.append(i)

while cardp_1 != deque([]) and cardp_2 != deque([]) and not special and rounds < 1000:
    p1 = cardp_1.popleft()
    p2 = cardp_2.popleft()
    war(cardp_1, cardp_2, p1, p2)
    rounds += 1

if special:
    print('PAT')
elif cardp_1 == deque([]):
    print(2,rounds)
elif cardp_2 == deque([]):
    print(1,rounds)