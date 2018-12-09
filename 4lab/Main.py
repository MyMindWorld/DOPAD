import re
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
def del_garbage():
    w = open("STU.txt", "w")
    with open("ServerToUser.txt", "r+") as f:
        for line in f:
            line = re.sub('[ ]', '', line)
            line1 = line.split(";")[1]
            w.write(''.join(line1)) # Каждое решение сервера в отдельную строку без лишних данных
    w = open("UTS.txt", "w")
    c = 0
    with open("UserToServer.txt", "r+") as f:
        for line in f:
            c +=1
            line = re.sub('[ ]', '', line)
            line1 = line.split(",")[2]
            if c < 7:
                line1 = line1.replace("\n", '')
            else:
                line1 = line1 + '\n'
                c = 0
            w.write(''.join(line1))  # Каждое решение сервера в отдельную строку без лишних данных

def compare():
    c = 0
    w = open("UTS_answers.txt", "w")
    with open("UTS.txt", "r+") as f:
        for line in f:
            c +=1
            if line == '\n':
                error =+ 1
            else:
                i = eval(str(line))
                w.write(str(i))
                if c != 79:
                    w.write('\n')
    w.close()
    f.close()
    with open("UTS_answers.txt", "r+") as f1, \
         open("STU.txt", "r+") as f2:
            for real, server in zip(f1, f2):  # читать построчно оба файла
                c += 1
                if real != server:
                    print('В выражении №', c, ' ошибка', real, ' не равно', server)

compare()