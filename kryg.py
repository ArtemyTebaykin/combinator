N = int(input("Введите N:"))
M = int(input("Введите M:"))
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
print(spisok[0])