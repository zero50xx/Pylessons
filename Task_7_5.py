import json
aver = 0
dct = {}
dct2 = {}
lst = []
with open("task_7_5.txt", "r", encoding = 'utf-8') as myfile:
    lines = myfile.readlines()
    for i in range(len(lines)):
        zz = lines[i].split()
        dct[zz[0]] = int(zz[2]) - int(zz[3])
        aver = aver + (int(zz[2]) - int(zz[3]))
    dct2['aver'] = aver / (len(lines)+1)
    lst.append(dct)
    lst.append(dct2)
        

with open("task_7_5_1.txt", "w", encoding = 'utf-8') as myfile:
    myfile.write(json.dumps(lst))

