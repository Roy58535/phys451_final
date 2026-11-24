from ..circuit import *
import matplotlib.pyplot as plt

ng_arr = np.linspace(-2, 2, 101)
e0 = np.zeros(101)
e1 = np.zeros(101)
e2 = np.zeros(101)

for i in range(101):
    e, s = solve_circuit(0.30, 100, ng_arr[i], 10)
    e0[i] = e[0]
    e1[i] = e[1]
    e2[i] = e[2]

plt.figure()
plt.plot(ng_arr, e0)
plt.plot(ng_arr, e1)
plt.plot(ng_arr, e2)
plt.show()
