import string


def check_room(line):
    char_freq = {}
    raw_words = line.split('-')
    for word in raw_words:
        for char in word:
            if char.isdecimal():
                sector_id, checksum = word.rstrip(']\n').split('[')
                sorted_freq = sorted(char_freq.items(), key=lambda kv: (-kv[1], kv[0]))
                # compare checksum to sorted freq of chars
                for i in range(0, len(checksum)):
                    if checksum[i] != sorted_freq[i][0]:  # mismatch found
                        return None
                return sector_id, raw_words  # they match
            else:
                if char in char_freq:
                    char_freq[char] += 1
                else:
                    char_freq[char] = 1


def decrypt_room(decrypt_factor, raw_words):
    answer = ''
    shift = decrypt_factor % 26
    translation_array = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    for word in raw_words:
        for char in word:
            if char.isdecimal():
                return answer
            else:
                answer += translation_array[ord(char) - ord('a')]
        answer += ' '


file = open("input.txt")
lines = file.readlines()
count = 0
for candidate in lines:
    valid_room = check_room(candidate)
    if valid_room is not None:
        # print(decrypt_room(int(valid_room[0]), valid_room[1]), valid_room[0])
        if decrypt_room(int(valid_room[0]), valid_room[1])[0] == 'n':  # just to find the north pole
            print(decrypt_room(int(valid_room[0]), valid_room[1]), valid_room[0])
            print('NORTH POLE CANDIDATE ABOVE ^')
