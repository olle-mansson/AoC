def correct_abba_sequence(l, i):
    return l[i] == l[i-3] and l[i-1] == l[i-2] != l[i]


def correct_aba_sequence(l, i):
    return l[i] == l[i-2] and l[i] != l[i-1]


def valid_tsl(line):
    in_brackets = False
    condition_met = False
    for i in range(3, len(line)):
        if in_brackets:
            if line[i] == ']':
                in_brackets = False
            elif correct_abba_sequence(line, i):
                condition_met = False
                break
        elif line[i] == '[':
            in_brackets = True
        elif correct_abba_sequence(line, i):
            condition_met = True
    return condition_met


def number_of_valid_tsl(file):
    count = 0
    for line in file:
        if valid_tsl(line):
            count += 1
    return count


def valid_ssl(line):
    in_brackets = False
    out_bracket_cand = set()
    in_bracket_cand = []
    for i in range(2, len(line)):
        if in_brackets:
            if line[i] == ']':
                in_brackets = False
            elif correct_aba_sequence(line, i):
                in_bracket_cand.append("".join(str(x) for x in line[i-2:i+1]))
        elif line[i] == '[':
            in_brackets = True
        elif correct_aba_sequence(line, i):
            out_bracket_cand.add(str(line[i - 1]) + str(line[i]) + str(line[i-1]))
    for cand in in_bracket_cand:
        if cand in out_bracket_cand:
            return True
    return False


def number_of_valid_ssl(file):
    count = 0
    for line in file:
        if valid_ssl(line):
                count += 1
    return count

print("Number of IP's with valid TSL's", number_of_valid_tsl(open("input.txt")))
print("Number of IP's with valid SSL's", number_of_valid_ssl(open("input.txt")), "\n")
