file = open('input.txt')


def is_triangle(triangle):
    sorted_triangle = sorted(triangle)
    return sorted_triangle[2] < sorted_triangle[0] + sorted_triangle[1]


lines = file.readlines()
count = 0
numbers = []
for line in lines:
    numbers.extend([int(x) for x in line.rstrip('\n').split()])
    if len(numbers) == 9:
        for i in range(0, 3):
            if is_triangle([numbers[i], numbers[i + 3], numbers[i + 6]]):
                count += 1
        numbers = []
print(count)
