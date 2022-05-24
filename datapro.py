import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 22})
T = []
CX1, CX2, CX3, CX4, CX5, CX6, CX7 = [], [], [], [], [], [], []

with open(r'data/cx.txt', 'r') as fp:
    for line in fp:
        t, cx1, cx2, cx3, cx4, cx5, cx6, cx7 = list(map(float, line.split()))
        T.append(t)
        CX1.append(cx1)
        CX2.append(cx2)
        CX3.append(cx3)
        CX4.append(cx4)
        CX5.append(cx5)
        CX6.append(cx6)
        CX7.append(cx7)

plt.plot(T, CX1, label='cx1')
plt.plot(T, CX2, label='cx2')
plt.plot(T, CX3, label='cx3')
plt.plot(T, CX4, label='cx4')
plt.plot(T, CX5, label='cx5')
plt.plot(T, CX6, label='cx6')
plt.plot(T, CX7, label='cx7')

plt.xlabel('Time (s)')
plt.ylabel('Concentration ($kg/m^3$)')

plt.legend()
plt.show()
