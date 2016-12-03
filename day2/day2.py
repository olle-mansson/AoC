file = open('input_test.txt')
lines = file.readlines()
code = []
current_pos = 5
for line in lines:
    for order in line:
        if order == 'U' and current_pos > 3:
            current_pos -= 3
        elif order == 'D' and current_pos < 7:
            current_pos += 3
        elif order == 'L' and current_pos % 3 != 1:
            current_pos -= 1
        elif order == 'R' and current_pos % 3 != 0:
            current_pos += 1

    code.append(current_pos)
print(code)
