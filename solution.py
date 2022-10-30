f = open('input.txt', 'rt')
s = f.readline().strip()
m = [int(k) for k in s.split(' ')]
m0 = m[0]
m1 = m[1]
s = f.readline().strip()
m = [float(k) for k in s.split(' ')]
d = 0
a = [0]*m0

for i in range (m0):
    a[i] = [0]*m1
for i in range(m0):
    for j in range(m1):
        a[i][j] = m[d]
        d += 1

s = f.readline().strip()
m = [int(k) for k in s.split(' ')]
m0 = m[0]
m1 = m[1]
s = f.readline().strip()
m = [float(k) for k in s.split(' ')]
d = 0
b = [0]*m0

for i in range (m0):
    b[i] = [0]*m1
for i in range(m0):
    for j in range(m1):
        b[i][j] = m[d]
        d += 1

s = f.readline().strip()
m = [int(k) for k in s.split(' ')]
m0 = m[0]
m1 = m[1]
s = f.readline().strip()
m = [float(k) for k in s.split(' ')]
d = 0
c = [0]*m0

for i in range (m0):
    c[i] = [0]*m1
for i in range(m0):
    for j in range(m1):
        c[i][j] = m[d]
        d += 1

const = float(f.readline().strip())

for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = b[i][j]*const

n = [[0 for j in range (len(c))] for i in range(len(c[0]))]
for i in range(len(c)):
    for j in range(len(c[i])):
        n[j][i] = c[i][j]

if len(b) != len(n) or len(n[0]) != len(b[0]):
    with open("output.txt", "w") as f:
        f.write("0\n")
    f.close()
    exit()

else:
    for i in range(len(b)):
        for j in range(len(b[i])):
              b[i][j] = n[i][j] + b[i][j]

if len(a[0]) != len(b):
    with open("output.txt", "w") as f:
        f.write("0\n")
    f.close()
    exit()

else:
    R = [0]*len(a)
    for i in range (len(a)):
        R[i] = [0]*len(b[0])

for g in range(len(b)):
    for i in range(len(a)):
        for j in range(len(b[0])):
            R[i][j] = R[i][j] + a[i][g] * b[g][j]

with open("output.txt", "w") as f:
    f.write("1\n")
    f.write(str(len(R)))
    f.write(" ")
    f.write(str(len(R[0])))
    f.write("\n")
    for i in range(len(R)):
        for j in range(len(R[0])):
            if R[i][j]%1==0:
                f.write(str(int(R[i][j])))
            else:
                f.write(str(R[i][j]))
            f.write(" ")

f.close()
