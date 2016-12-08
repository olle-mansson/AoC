def create_rect(size, grid):
    for i in range(size[1]):
        for j in range(size[0]):
            grid[i][j] = u"\u2588"
    return grid


def rotate_row(row, shift, grid):
    shift %= 50
    old_row = grid[row]
    new_row = old_row[-shift:] + old_row[:len(old_row) - shift]
    grid[row] = new_row
    return grid


def rotate_col(col, shift, grid):
    shift %= 6
    old_col = [row[col] for row in grid]
    new_col = old_col[-shift:] + old_col[:len(old_col) - shift]
    for i in range(len(new_col)):
        grid[i][col] = new_col[i]
    return grid


def parse_line(line, grid):
    args = str(line).strip().split(' ')
    if args[0] == "rect":
        grid = create_rect([int(x) for x in args[1].split('x')], grid)
    elif args[1] == "row":
        grid = rotate_row(int(args[2].lstrip('y=')), int(args[4]), grid)
    else:
        grid = rotate_col(int(args[2].lstrip('x=')), int(args[4]), grid)
    return grid


def main():
    file = open("input.txt")
    grid = [[u"\u2591" for x in range(50)] for x in range(6)]
    count = 0
    for line in file:
        grid = parse_line(line, grid)
    for row in grid:
        for element in row:
            print(element, sep='', end='')
            if element == u"\u2588":
                count += 1
        print()
    print("\nPixels lit:", count)


main()
