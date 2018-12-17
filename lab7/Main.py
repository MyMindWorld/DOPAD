import hashlib
i = 0
while True:
    log = 'log'
    filename = "_".join([log, str(i)])
    f = open(filename, 'w')
    i += 1
    names = 'Pavel', 'Efim'
    name_1 = input('Enter Name ')
    pay_1 = int(input('Enter Salary '))
    long_1 = int(input('Enter Time of work '))
    name_2 = input('Enter Name ')
    pay_2 = int(input('Enter Salary '))
    long_2 = int(input('Enter Time of work '))
    name_3 = input('Enter Name ')
    pay_3 = int(input('Enter Salary '))
    long_3 = int(input('Enter Time of work '))
    if name_1 in names:
        pay_1 = pay_1 * 2
    if name_2 in names:
        pay_2 = pay_2 * 2
    if name_3 in names:
        pay_3 = pay_3 * 2
    if pay_1 * long_1 == 777:
        print('The', name_1, 'is BLESSED!')
    if pay_2 * long_2 == 777:
        print('The', name_2, 'is BLESSED!')
    if pay_3 * long_3 == 777:
        print('The', name_3, 'is BLESSED!')
    print('№ Name Salary Long PayAll')
    f.write('N Name Salary Long PayAll\n')
    print('1 ', name_1, ' ', pay_1, '  ', long_1, '  ', pay_1 * long_1)
    out = str((1, name_1, pay_1, long_1, pay_1 * long_1))
    f.write(out + '\n')
    print('2 ', name_2, '  ', pay_2, '  ', long_2, '  ', pay_2 * long_2)
    out = str((2, name_2, pay_2, long_2, pay_2 * long_2))
    f.write(out + '\n')
    print('3 ', name_3, '  ', pay_3, '  ', long_3, '  ', pay_3 * long_3)
    out = str((3, name_3, pay_3, long_3, pay_3 * long_3))
    f.write(out + '\n')
    if i % 5 == 0:
        print('Купите нашего слона всего за', pay_1 * long_1)
    if i % 2 == 0:
        hash = hashlib.md5(b"Pavel").digest()
        with open('mining.txt', 'w+') as mine:
            mine.write(str(hash))
        print(hash)
