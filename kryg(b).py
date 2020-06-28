N = int(input("Введите N:"))
M = int(input("Введите M:"))
L1 = int(input("Введите L:"))
m = M
spisok = []
for i in range(N):
    spisok.append((i+1))
ch = 0
while spisok[0] != spisok[-1]:
    if M > len(spisok):
        while M > len(spisok):
            M = M - len(spisok)
    if M > (len(spisok)-ch):
        while M > (len(spisok)-ch):
            ch = ch - (len(spisok))
    ch = ch + M - 1
    spisok.pop(ch)
L2 = spisok[0]
if L1 - L2 >= 0:
    print(L1 - L2 + 1)
else:
    print(N + (L1 - L2) + 1)