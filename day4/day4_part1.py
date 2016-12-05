def check_room(candidate):
    char_freq = {}
    raw_words = candidate.split('-')
    for word in raw_words:
        for char in word:
            if char.isdecimal():
                sector_id, checksum = word.rstrip(']\n').split('[')
                sorted_freq = sorted(char_freq.items(), key=lambda kv: (-kv[1], kv[0]))
                # compare checksum to sorted freq of chars
                for i in range(0, len(checksum)):
                    if checksum[i] != sorted_freq[i][0]:  # mismatch found
                        return 0
                return sector_id  # they match
            else:
                if char in char_freq:
                    char_freq[char] += 1
                else:
                    char_freq[char] = 1


file = open("input.txt")
count = 0
for line in file:
    count += int(check_room(line))
print(count)
