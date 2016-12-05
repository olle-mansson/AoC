import hashlib
door_ID = "ffykfhsq"
code = []
i = 0
while len(code) < 8:
    i += 1
    m = hashlib.md5((door_ID + str(i)).encode('utf-8')).hexdigest()
    if m[0:5] == "00000":
        code.append(m[5])
        print("".join(str(x) for x in code), "".join('_'*(8-len(code))), sep='')

print('First password:', "".join(str(x) for x in code))

i = 0
real_length = 0
code = ['_']*8
index_done = {}
while real_length < 8:
    i += 1
    m = hashlib.md5((door_ID + str(i)).encode('utf-8')).hexdigest()
    if m[0:5] == "00000":
        if str(m[5]).isdecimal() and int(m[5]) < 8 and int(m[5]) not in index_done:
            index_done[int(m[5])] = 1
            code[int(m[5])] = m[6]
            real_length += 1
            print("".join(str(x) for x in code))

print('Second password:', "".join(str(x) for x in code))
