import timeit

file = open('input.txt')
all_lines = file.readlines()


def test1():
    solution_one(lines=all_lines)


def test2():
    solution_one(lines=all_lines)


def solution_one(lines):
    count = 0
    for line in lines:
        triangle = [int(x) for x in line.rstrip('\n').split()]
        sorted_triangle = sorted(triangle)
        if sorted_triangle[2] < sorted_triangle[0] + sorted_triangle[1]:
            count += 1
    return count


def solution_two(lines):
    count = 0
    for line in lines:
        triangle = [int(x) for x in line.rstrip('\n').split()]
        max_val = max(triangle)
        triangle.remove(max_val)
        if max_val < triangle[0] + triangle[1]:
            count += 1
    return count


print('Solution one took: ', min(
    timeit.repeat("test1()", setup="from __main__ import test1", number=50, repeat=10)))
print('Solution two took: ', min(
    timeit.repeat("test2()", setup="from __main__ import test2", number=50, repeat=10)))

# seems like there are no performance penalty to choosing sorted()
print('\nAnswer:\n', solution_one(all_lines))
