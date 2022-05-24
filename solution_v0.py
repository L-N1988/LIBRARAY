import numpy
import math
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set_theme()

B, L = 5, 250
dx, dy = 0.5, 0.5
N, M = int(L/dx), int(B/dy)

g = 9.8
tmax = 3600

h = numpy.zeros((N, M)) + 1.0
u = numpy.zeros((N, M)) + 0.5

Kx = numpy.zeros((N, M)) + 0.05
Ky = numpy.zeros((N, M)) + 0.05

cnow = numpy.zeros((N, M))
cnew = numpy.zeros((N, M))

umax = numpy.max(u + numpy.sqrt(g*h))

t1, t2, t3, t4, t5 = 100, 900, 1800, 3000, 3599

for i in range(N):
    for j in range(M):
        if i*dx < 5.0 and abs(j*dy - 2.5) < 1:
            cnow[i][j] = 0.1;

T = []
cx1, cx2, cx3, cx4, cx5, cx6, cx7 = [], [], [], [], [], [], []
time = 0

# plt.figure(figsize=(20, 20))
# ax = sns.heatmap(cnow, cmap="RdBu_r")
# ax.annotate('t = %04.1f s'%(time),
#             xy=(10, 10), xycoords='figure pixels', fontsize=30)
# plt.savefig("figures/pollution/pollution_%05.1f.png"%(time))


while time < tmax:
    dt = dx / umax
    # end point is false
    for i in range(1, N-1):
        for j in range(1, M-1):
            temp1 = h[i][j]*Kx[i][j]*(cnow[i+1][j]+cnow[i-1][j]-2.0*cnow[i][j]) / (dx**2)
            temp2 = h[i][j]*Ky[i][j]*(cnow[i][j+1]+cnow[i][j-1]-2.0*cnow[i][j]) / (dy**2)
            temp3 = h[i][j]*u[i][j]*(cnow[i+1][j]-cnow[i-1][j]) / (2*dx)
            cnew[i][j] = cnow[i][j] + (temp1+temp2-temp3)*dt/h[i][j]
    for j in range(M):
        if abs(j*dy -5) < 0.6:
            cnew[0][j] = math.sin(time/1000) * 0.6
    cnew[N-1, :] = cnew[N-2, :]
    cnew[:, M-1] = cnew[:, M-2]
    cnew[:, 0] = cnew[:, 1]

    print("time: ", time)
    time += dt
    # if abs(time - (int(time)+0.5)) < 0.2:
    #     if time > 0 and time < 100:
    #         # changing the size of figure
    #         plt.figure(figsize=(20, 20))
    #         ax = sns.heatmap(cnew, cmap='RdBu_r')
    #         ax.annotate('t = %04.1f s'%(time),
    #                 xy=(10, 10), xycoords='figure pixels', fontsize=30)
    #         plt.savefig("figures/pollution/pollution_%05.1f.png"%(time))
    if (time-t1) * (time - t1 -dt) < 0:
        ct1 = cnow;
        ct1.tofile('data/ct1.txt')
    if (time-t2) * (time - t2 -dt) < 0:
        ct2 = cnow;
        ct2.tofile('data/ct2.txt')
    if (time-t3) * (time - t3 -dt) < 0:
        ct3 = cnow;
        ct3.tofile('data/ct3.txt')
    if (time-t4) * (time - t4 -dt) < 0:
        ct4 = cnow;
        ct4.tofile('data/ct4.txt')
    if (time-t5) * (time - t5 -dt) < 0:
        ct5 = cnow;
        ct5.tofile('data/ct5.txt')

    T.append(time)
    cx1.append(cnew[  1][5])
    cx2.append(cnew[ 10][5])
    cx3.append(cnew[ 20][5])
    cx4.append(cnew[ 30][5])
    cx5.append(cnew[ 50][5])
    cx6.append(cnew[ 80][5])
    cx7.append(cnew[100][5])
    cnow = cnew

# open file in write mode
with open(r'data/cx.txt', 'w') as fp:
    for tt, c1, c2,c3, c4, c5, c6, c7 in zip(T, cx1, cx2, cx3, cx4, cx5, cx6, cx7):
        # write each item on a new line
        fp.write("%f %f %f %f %f %f %f %f\n" % (tt, c1, c2,c3, c4, c5, c6, c7))
print('Done')
