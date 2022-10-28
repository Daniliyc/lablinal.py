f = open('input.txt','rt')
mas = f.readline().split()
a, b, c, d, p, q = mas[0], mas[1], mas[2], mas[3], mas[4], mas[5]
a, b, c, d, p, q = float(a), float(b), float(c), float(d), float(p), float(q)
mat = [[a, b],
       [c, d]]
matb = [[p],
        [q]]
matx = [[p,b],
        [q,d]]
maty = [[a, p],
        [c, q]]
det_mat = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
det_matx = matx[0][0] * matx[1][1] - matx[1][0] * matx[0][1]
det_maty = maty[0][0] * maty[1][1] - maty[1][0] * maty[0][1]
if det_mat != 0:
    x = det_matx / det_mat
    y = det_maty / det_mat
    k = '2 ' + str(x) + ' ' + str(y)
    f = open('output.txt','w')
    f.write(k)
elif mat[0][1] == mat[1][1] == 0:
    x = matb[0][0] / mat[0][0]
    k = '3 ' + str(x)
    f = open('output.txt','w')
    f.write(k)
elif  mat[0][0] == mat[1][0] == 0:
    y = matb[0][0] / mat[0][1]
    k = '4 ' + str(y)
    f = open('output.txt','w')
    f.write(k)
elif mat[0][0] == mat[0][1] == mat[1][0] == mat[1][1] == 0:
    f = open('output.txt','w')
    f.write('5')
elif det_mat == det_matx == det_maty == 0:
    if (mat[0][0] % mat[1][0] == 0) and (mat[0][1] % mat[1][1] == 0) and (matb[0][0] % matb[1][0] == 0):
            s = mat[0][0] / mat[0][1] * (-1)
            t = matb[0][0] / mat[0][1]
            k = '1 ' + str(s) + ' ' + str(t)
            f = open('output.txt','w')
            f.write(k)
    elif (mat[1][0] % mat[0][0] == 0) and (mat[1][1] % mat[0][1] == 0) and (matb[1][0] % matb[0][0] == 0):
            s = mat[1][0] / mat[1][1] * (-1)
            t = matb[1][0] / mat[1][1]
            k = '1 ' + str(s) + ' ' + str(t)
            f = open('output.txt','w')
            f.write(k)
else:
    f = open('output.txt','w')
    f.write('0')
f.close()
