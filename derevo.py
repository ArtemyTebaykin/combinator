N = int(input("Введите N:"))
M = int(input("Введите M:"))
spisok = []
for i in range(N):
    spisok.append((i+1))
ch = 0
while spisok[0] != spisok[-1]:
    while M > len(spisok):
        M = M - len(spisok)
    if M > (len(spisok)-ch):
        while M > (len(spisok)-ch):
            M = M - (len(spisok)-ch)
        spisok.pop(ch)
    else:
        ch += M
        spisok.pop(ch)
print(spisok)