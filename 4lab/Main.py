import re
from operator import itemgetter
from natsort import natsorted
def sort_and_format():
    uts_raw = []
    stu_raw = []
    uts = []
    stu = []
    with open('IKB_3_6.txt', 'r+') as f:
        for line in f:
            if 'Server_To_User' in line:
                stu_raw.append(line)
            if 'User_To_Server' in line:
                uts_raw.append(line)
    for line in stu_raw:
        str(line)
        line = re.sub('["=]', '', line)
        line = re.sub('[,]', ';', line)
        stu.append(re.compile("\((.*)\)").search(line).group(1))
    for line in uts_raw:
        str(line)
        line = re.sub('["]', '', line)
        uts.append(re.compile("\((.*)\)").search(line).group(1))
    stu = natsorted(stu)
    #print('\n'.join(stu))
    w = open("ServerToUser.txt", "w")
    w.write('\n'.join(stu))
    uts = natsorted(uts)
    #print('\n'.join(uts))
    w = open("UserToServer.txt", "w")
    w.write('\n'.join(uts))
def find_mistakes():
    w = open("STU.txt", "w")
    with open("ServerToUser.txt", "r+") as f:
        for line in f:
            line = re.sub('[ ]', '', line)
            line1 = line.split(";")[1]
            print(line1)
            w.write(''.join(line1)) # Каждое решение сервера в отдельную строку без лишних данных
find_mistakes()