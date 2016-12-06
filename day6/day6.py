def rep_code(file, function):
    msg_len = len(file.readline().rstrip('\n'))
    # reset file
    file.seek(0)
    default = -function([-200, 200])
    # init a nested list, cumbersome in python!
    msg_char_freq = [[default for x in range(26)] for x in range(msg_len)]

    for line in file:
        for i in range(0, msg_len):
            if msg_char_freq[i][ord(line[i]) - ord('a')] is default:
                msg_char_freq[i][ord(line[i]) - ord('a')] = 1
            else:
                msg_char_freq[i][ord(line[i]) - ord('a')] += 1

    msg = ""
    for char_freq in msg_char_freq:
        msg += chr(char_freq.index(function(char_freq)) + ord('a'))
    return msg

print(rep_code(open('input.txt'), max))
print(rep_code(open('input.txt'), min))
