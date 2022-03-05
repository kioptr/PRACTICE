import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevator_positions = []
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_positions.append([int(j) for j in input().split()])
elevator_positions.sort()
primeira = True
round = 3
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT
    if round == 3:
        #asd
        if exit_floor == clone_floor:
            if direction == 'LEFT':
                if exit_pos <= clone_pos:
                    print('WAIT')
                else:
                    print('BLOCK')
            else:
                if exit_pos >= clone_pos:
                    print('WAIT')
                else:
                    print('BLOCK')
        else:
            for coord in elevator_positions:
                if coord[0] == clone_floor:
                    next_pos = coord[1]
                    if direction == 'LEFT':
                        if next_pos <= clone_pos:
                            print('WAIT')
                        else:
                            print('BLOCK')
                    else:
                        if next_pos >= clone_pos:
                            print('WAIT')
                        else:
                            print('BLOCK')
        #primeira = False
        print("Debug messages...", file=sys.stderr, flush=True)
        round = 0
    else: print('WAIT')
    round += 1