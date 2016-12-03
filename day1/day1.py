import numpy as np


def travel(filename):
    f = open(filename)
    inputs = f.read().split(', ')
    curr_direction = np.array([0, 1])
    curr_position = np.array([0, 0])
    left_rot = np.array([[0, -1],
                        [1, 0]])
    right_rot = np.array([[0, 1],
                         [-1, 0]])
    visited_positions = {curr_position.tostring(): 1}
    for order in inputs:
        if order[0] == 'R':
            curr_direction = np.dot(right_rot, curr_direction)
        else:
            curr_direction = np.dot(left_rot, curr_direction)
        for i in range(0, int(order[1:])):
            curr_position += curr_direction
            if curr_position.tostring() in visited_positions:
                return curr_position
            else:
                visited_positions[curr_position.tostring()] = 1
    return curr_position


filename = 'directions.txt'
final_position = travel(filename)
print(final_position)
print(abs(final_position[0]) + abs(final_position[1]))
