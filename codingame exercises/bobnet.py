import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
conexoes = []
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    conexoes.append([n1,n2])
gates = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gates.append(ei)

# game loop
while True:
    agent = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    for liga in conexoes:
        if agent in liga:
            for i in gates:
                if i in liga:
                    print(liga[0],liga[1])
        else:
            print(0,1)