import timeit

file = open('input.txt')
all_lines = file.readlines()


def test1():
    solution_one(lines=all_lines)


def test2():
    solution_two(lines=all_lines)


def test3():
    solution_three(lines=all_lines)


def solution_one(lines):
    count = 0
    for line in lines:
        t = [int(x) for x in line.rstrip('\n').split()]
        st = sorted(t)
        if st[2] < st[0] + st[1]:
            count += 1
    return count


def solution_two(lines):
    count = 0
    for line in lines:
        t = [int(x) for x in line.rstrip('\n').split()]
        max_val = max(t)
        t.remove(max_val)
        if max_val < t[0] + t[1]:
            count += 1
    return count


def solution_three(lines):
    count = 0
    for line in lines:
        t = [int(x) for x in line.rstrip('\n').split()]
        if t[0] + t[1] > t[2] and t[1] + t[2] > t[0] and t[0] + t[2] > t[1]:
            count += 1
    return count


print('Solution one took: ', min(
    timeit.repeat("test1()", setup="from __main__ import test1", number=500, repeat=5)))
print('Solution two took: ', min(
    timeit.repeat("test2()", setup="from __main__ import test2", number=500, repeat=5)))
print('Solution three took: ', min(
    timeit.repeat("test3()", setup="from __main__ import test3", number=500, repeat=5)))
# seems like there are no performance penalty to choosing sorted()

print('\nAnswer one:\n', solution_one(all_lines))
print('\nAnswer two:\n', solution_two(all_lines))
print('\nAnswer three:\n', solution_three(all_lines))
