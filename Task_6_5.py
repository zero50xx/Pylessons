
i = 0
zz = []
sm = 0
dct = {}
with open("task_6_5.txt", "r", encoding = 'utf-8') as myfile:
    lines = myfile.readlines()
    for j in range(len(lines)):
        sm = 0
        integ = []
        zz = lines[j].split()
        i = 0
        l = len(lines[j])
        while i < l:
            s_int = ''
            a = lines[j][i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < l:
                    a = lines[j][i]
                else:
                    break
            i += 1
            if s_int != '':
                integ.append(int(s_int))
        for z in range(len(integ)):
            sm = sm + int(integ[z])
        dct[zz[0]] = sm



print(dct)