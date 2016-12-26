import numpy as np
import scipy as sp
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

import matplotlib

# test exit
import sys

matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import matplotlib.pyplot as plt

L_glob = np.array([1.5, 0.5])

elem = np.array([0, 1, 2])
# Délky jednotlivých prvků Vše přeložit do ajiny nakonec jako vždy
E = 210000000000.
A = 0.12
I_y = 0.01
q = 1000000.
n0 = 0.
kx = 0.
ky = 0
L = np.array([0.666, 0.666, 0.666])
# uzly souřadnice pro prvky?
nodes = np.array([])

for i in range(0, len(L)):
    nodes = np.append(nodes, np.sum(L[:i]))
    nodes = np.append(nodes, np.sum(L[:(i + 1)]))
print(nodes)

# pro barovej graf!!
nodes1 = np.array([])
for i in range(0, len(L)):
    nodes1 = np.append(nodes1, np.sum(L[:i]))
print('NOD9KY')
print(nodes1)
# split na počet prvků!!!
mid_nodes = np.array_split(nodes, 3)
mid_nodes_ = np.array([])
for i in range(0, len(mid_nodes)):
    _a = (mid_nodes[i][0] + mid_nodes[i][1]) / 2
    mid_nodes_ = np.append(mid_nodes_, _a)
print(mid_nodes_)

# nevim zda tu celkovou delku nějak použiju?
"""
L_glob = np.array([])
for i in range(0, len(L)):
    if i == 0:
        L_glob = np.append(L_glob, L[i])
    else:
        L_glob = np.append(L_glob, L_glob[i - 1] + L[i])
"""

I = np.array([])
J = np.array([])
K = np.array([])
# Array with indices of vector transformation..have to find another solution probably
fij = np.array([])
f = np.array([])

# composing stiffness matrix
for i in elem:
    I = np.append(I,
                  [i * 3, i * 3, i * 3, i * 3, i * 3, i * 3, i * 3 + 1, i * 3 + 1, i * 3 + 1, i * 3 + 1, i * 3 + 1,
                   i * 3 + 1, i * 3 + 2, i * 3 + 2, i * 3 + 2, i * 3 + 2, i * 3 + 2, i * 3 + 2, i * 3 + 3, i * 3 + 3,
                   i * 3 + 3, i * 3 + 3, i * 3 + 3, i * 3 + 3, i * 3 + 4, i * 3 + 4, i * 3 + 4, i * 3 + 4, i * 3 + 4,
                   i * 3 + 4, i * 3 + 5, i * 3 + 5, i * 3 + 5, i * 3 + 5, i * 3 + 5, i * 3 + 5])
    J = np.append(J,
                  [i * 3, i * 3 + 1, i * 3 + 2, i * 3 + 3, i * 3 + 4, i * 3 + 5, i * 3, i * 3 + 1, i * 3 + 2, i * 3 + 3,
                   i * 3 + 4, i * 3 + 5, i * 3, i * 3 + 1, i * 3 + 2, i * 3 + 3, i * 3 + 4, i * 3 + 5, i * 3, i * 3 + 1,
                   i * 3 + 2, i * 3 + 3, i * 3 + 4, i * 3 + 5, i * 3, i * 3 + 1, i * 3 + 2, i * 3 + 3, i * 3 + 4,
                   i * 3 + 5, i * 3, i * 3 + 1, i * 3 + 2, i * 3 + 3, i * 3 + 4, i * 3 + 5])
    K = np.append(K,
                  [E * A / L[i] + kx * L[i] / 3, 0, 0, -E * A / L[i] + kx * L[i] / 6, 0, 0, 0,
                   12 * (E * I_y + ky) / L[i] ** 3,
                   6 * (E * I_y + ky) / L[i] ** 2, 0,
                   -12 * (E * I_y + ky) / L[i] ** 3,
                   6 * (E * I_y + ky) / L[i] ** 2, 0,
                   6 * (E * I_y + ky) / L[i] ** 2, 4 * (E * I_y + ky) / L[i], 0,
                   -6 * (E * I_y + ky) / L[i] ** 2, 2 * (E * I_y + ky) / L[i], -E * A / L[i] + kx * L[i] / 6, 0, 0,
                   E * A / L[i] + kx * L[i] / 3, 0, 0, 0,
                   -12 * (E * I_y + ky) / L[i] ** 3, -6 * (E * I_y + ky) / L[i] ** 2, 0, 12 * (E * I_y + ky) / L[i] ** 3,
                   -6 * (E * I_y + ky) / L[i] ** 2, 0, 6 * (E * I_y + ky) / L[i] ** 2,
                   2 * (E * I_y + ky) / L[i], 0, -6 * (E * I_y + ky) / L[i] ** 2,
                   4 * (E * I_y + ky) / L[i]])
    fij = np.append(fij, [i * 3, i * 3 + 1, i * 3 + 2, i * 3 + 3, i * 3 + 4, i * 3 + 5])
    f = np.append(f, [0.5 * n0 * L[i], (1 / 2) * q * L[i], (1 / 12) * q * L[i] ** 2, 0.5 * n0 * L[i],
                      (1 / 2) * q * L[i], (-1 / 12) * q * L[i] ** 2])
I = I.astype(int)
J = J.astype(int)
fij = fij.astype(int)
print('test glob vekt Ffij')
print(fij)
K_glob = coo_matrix((K, (I, J))).tolil()

f_glob = coo_matrix((f, (fij, fij))).tolil()
print('test glob vekt F')
print(f_glob.toarray().astype(int))
KKK = K_glob.toarray()
print(K_glob)
print(KKK)

# sys.exit("Test matic")
# TODO: Napsat univerzálně pro zadané boundary conditions

K_glob[0, :] = 0
K_glob[:, 0] = 0
K_glob[0, 0] = 1

K_glob[:, 1] = 0
K_glob[1, :] = 0
K_glob[1, 1] = 1

K_glob[:, 10] = 0
K_glob[10, :] = 0
K_glob[10, 10] = 1

K_glob = K_glob.tocsr()
# boundary
print(K_glob.toarray().astype(int))

f_glob_i, f_glob_j = f_glob.get_shape()

f_glob_vec = np.array([])
for i in range(f_glob_i):
    for j in range(f_glob_j):
        if i == j:
            f_glob_vec = np.append(f_glob_vec, f_glob[i, j])

print('globalni vekt')
print(f_glob_vec)
f_glob_vec[0] = 0
f_glob_vec[1] = 0
f_glob_vec[10] = 0
# test uzlové síly WORKING
#f_glob_vec[12] = 1
# [15] = 0.5

u = spsolve(K_glob, f_glob_vec)
# 11BS znamená počet dělení, kolik je uzlů na modelu!!
uu = np.array_split(u, 4)
print(uu)
M = np.array([])
V = np.array([])
N = np.array([])
for i in elem:
    n_1 = uu[i][0]
    v_1 = uu[i][1]
    w_1 = uu[i][2]
    n_2 = uu[i + 1][0]
    v_2 = uu[i + 1][1]
    w_2 = uu[i + 1][2]

    M0 = -E * I_y * (v_1 * (-6 / L[i] ** 2) + w_1 * (-4 / L[i]) + v_2 * (6 / L[i] ** 2) + w_2 * (-2 / L[i]))
    M = np.append(M, M0)
    ML = -E * I_y * (
        v_1 * (((12 * L[i]) / L[i] ** 3) - (6 / L[i] ** 2)) + w_1 * ((6 * L[i] / L[i] ** 2) - (4 / L[i])) + v_2 * (
            (6 / L[i] ** 2) - (12 * L[i] / L[i] ** 3)) + w_2 * ((6 * L[i] / L[i] ** 2) - (2 / L[i])))
    M = np.append(M, ML)
    VL = -E * I_y * (v_1 * 12 / L[i] ** 3 + w_1 * 6 / L[i] ** 2 - v_2 * 12 / L[i] ** 3 + w_2 * 6 / L[i] ** 2)
    V = np.append(V, VL)
    NL = ((E * A) / L[i]) * (n_2 - n_1)
    N = np.append(N, NL)
print('Momenty')
print(M)
print('Posouvacky')
print(V)
print('Normalovky')

print(N)

fig, ax1 = plt.subplots()

plt.xlabel(r'$L[m]$')
ax1.set_ylabel(r'$M[kNm]$')
plt.title(r'$\textit{Průběh vnitřních sil M, V}$')
# plt.xscale('log')
# plt.axis((10, 10000, 1, 3))

ax2 = ax1.twinx()
ax2.set_ylabel(r'$V[kN]$')

# plt.plot(nodes, M, c='k')
# plt.plot(mid_nodes_, V, c='b')
ax1.fill_between(nodes, 0, M, facecolor=(0, 0, 0, 0), where=M >= 0, hatch='|', edgecolor='k', interpolate=True)
ax1.fill_between(nodes, 0, M, facecolor=(0, 0, 0, 0), where=0 >= M, hatch='|', edgecolor='m', interpolate=True)
ax2.fill_between(mid_nodes_, 0, V, facecolor=(0, 0, 0, 0), where=V >= 0, hatch='|', edgecolor='b', interpolate=True)
ax2.fill_between(mid_nodes_, 0, V, facecolor=(0, 0, 0, 0), where=0 >= V, hatch='|', edgecolor='r', interpolate=True)

ax2.bar(nodes1, N, L)
# normálovky
# ax2.fill_between(mid_nodes_, 0, N, facecolor=(0, 0, 0, 0), hatch='-', interpolate=True)
lgd1 = ax1.legend(['M+', 'M-'], loc='upper right')
lgd2 = ax2.legend(['V-', 'V+', 'N'], loc='lower right')
# ax2.set_ylim(ax1.get_ylim())
# funkce na limit os, a zarovnání!
"""""""""
limit1 = [0, 0]
limit2 = [0, 0]
ax1_ = ax1.get_ylim()
ax2_ = ax2.get_ylim()
if abs(ax1_[0]) < abs(ax2_[1]):
    limit1[0] = -abs(ax2_[1])
    limit2[1] = ax2_[1]
else:
    limit1[0] = -abs(ax1_[0])
    limit2[1] = ax1_[0]

if abs(ax2_[0]) < abs(ax1_[1]):
    limit1[1] = abs(ax1_[1])
    limit2[0] = ax2_[1]
else:
    limit1[1] = abs(ax2_[0])
    limit2[0] = ax2_[0]

ax1.set_ylim(limit1)
ax2.set_ylim(limit2)
ax1.invert_yaxis()
"""""""""
plt.axhline(0, color='black')

plt.savefig('plot.png', bbox_extra_artists=(lgd1, lgd2), bbox_inches='tight')
# ML =
# f = sp.vstack([x.T.tolil().reshape(fij.shape) for x in f_glob])
