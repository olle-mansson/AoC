import numpy as np


file = open('input.txt')
lines = file.readlines()
code = []
allowed_positions = {np.array([0, 2]).tostring(): 1, np.array([-1, 1]).tostring(): 2, np.array([0, 1]).tostring(): 3,
                     np.array([1, 1]).tostring(): 4, np.array([-2, 0]).tostring(): 5, np.array([-1, 0]).tostring(): 6,
                     np.array([0, 0]).tostring(): 7, np.array([1, 0]).tostring(): 8, np.array([2, 0]).tostring(): 9,
                     np.array([-1, -1]).tostring(): 'A', np.array([0, -1]).tostring(): 'B',
                     np.array([1, -1]).tostring(): 'C', np.array([0, -2]).tostring(): 'D'}

current_pos = np.array([-2, 0])

for line in lines:
    for order in line:
        if order == 'U' and (current_pos + np.array([0, 1])).tostring() in allowed_positions:
            current_pos += np.array([0, 1])
        elif order == 'D' and (current_pos + np.array([0, -1])).tostring() in allowed_positions:
            current_pos += np.array([0, -1])
        elif order == 'L' and (current_pos + np.array([-1, 0])).tostring() in allowed_positions:
            current_pos += np.array([-1, 0])
        elif order == 'R' and (current_pos + np.array([1, 0])).tostring() in allowed_positions:
            current_pos += np.array([1, 0])
    code.append(allowed_positions[current_pos.tostring()])

print(code)
