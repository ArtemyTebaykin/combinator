import copy
spisok1 = input("Введите списки через пробел:").split()
#spisok1 = ['abc', '123']
spisok2 = []
for i in spisok1:
    i = [i]
    spisok2.append(i)
kol_sp = len(spisok2)
spisok3 = []
for a in spisok2:
    for b in a:
        for c in b:
            c = [c]
            spisok3.append(c)
spisok_ch = []
for s in spisok2:
    for c in s:
        spisok_ch.append(len(c))
spisok4 = []
while spisok_ch != []:
    pr = spisok_ch[0]
    spisok4.append(spisok3[0:(pr)])
    for w in range(pr):
        spisok3.pop(0)
    spisok_ch.pop(0)
spisok6 = []
for gg in spisok1:
    for ss in gg:
        spisok6.append(ss)
sp6 = copy.deepcopy(spisok6)
spisok5 = []
if len(spisok1) == 2:
    u = len(spisok4[0])
    del sp6[:(u)]
    for ii in spisok4[0]:
        for jj in sp6:
            aaa = ii[0] + jj
            aaa = [aaa]
            spisok5.append(aaa)
else:
    while len(spisok1) != 1:
        u = len(spisok4[0])
        del sp6[:(u)]
        for ii in spisok4[0]:
            for jj in sp6:
                aaa = ii[0] + jj
                aaa = [aaa]
                spisok5.append(aaa)
        spisok4.pop(0)
        spisok1.pop(0)
print(spisok5)