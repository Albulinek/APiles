import numpy as np
import os

import matplotlib

# test exit
import sys
import io

matplotlib.rcParams['text.usetex'] = True
matplotlib.rc('font', family='sans-serif')
matplotlib.rc('font', serif='Helvetica Neue')
matplotlib.rc('text', usetex='false')
matplotlib.rcParams['text.latex.unicode'] = True
import matplotlib.pyplot as plt


def dbgPrint(console, *objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    # ignore file, uses StringIO API
    sIO = io.StringIO()
    print(*objects, sep=sep, end=end, file=sIO, flush=flush)
    console.insertPlainText(sIO.getvalue())
    sIO.close()


def MKP(L_glob, console, BC, len_fem, bend_force, ver_force, hor_force, edefpile, diameter, L_glob_soil, E_def_soil, ky_soil, kx_soil, beta_soil, const, ky_foot):
    # input verification
    for i in range(0, len(L_glob)):
        if L_glob[i] == 0:
            dbgPrint(console, 'Některý díl piloty má nastavenou nulovou výšku')
            return None
        else:
            pass

    for i in range(0, len(L_glob_soil)):
        if L_glob_soil[i] == 0:
            dbgPrint(console, 'Některá vrstva má nastavenou nulovou výšku')
            return None
        else:
            pass


    L = np.array([])
    elem = np.array([])
    edpile = np.array([])
    apile = np.array([])
    Jypile = np.array([])
    diameter_mod = np.array([])

    for i in range(0, len(L_glob)):
        count = int(np.around(L_glob[i] / float(len_fem)))
        for j in range(0, count):
            L = np.append(L, L_glob[i] / count)
            edpile = np.append(edpile, edefpile[i])
            diameter_mod = np.append(diameter_mod, diameter[i])
            Jypile = np.append(Jypile, (1 / 4) * np.pi * (diameter[i] / 2) ** 4)
            apile = np.append(apile, np.pi * diameter[i]**2)

    L_soil_modified = np.array([])
    beta_modified = np.array([])
    edefsoil_modified = np.array([])
    ky_soil_modified = np.array([])
    kx_soil_modified = np.array([])

    for i in range(0, len(L_glob_soil)):
        count = int(np.around(L_glob_soil[i] / float(len_fem)))
        for j in range(0, count):
            L_soil_modified = np.append(L_soil_modified, L_glob_soil[i] / count)
            beta_modified = np.append(beta_modified, beta_soil[i])
            edefsoil_modified = np.append(edefsoil_modified, E_def_soil[i])
            ky_soil_modified = np.append(ky_soil_modified, ky_soil[i])
            if not const:
                kx_soil_modified = np.append(kx_soil_modified, kx_soil[i])
    print(ky_soil_modified)
    print(kx_soil_modified)


    kx_soil_recount = np.array([])
    # horizontal stiffness
    if const:
        for i in range(0,len(L)):
            kx_soil_recount = np.append(kx_soil_recount, (3*edefsoil_modified[i])/(2*(diameter_mod[i]+2*diameter_mod[i]*np.tan(np.radians(beta_modified[i])))))
        dbgPrint(console, 'Navržené hodnoty Kx:')
        dbgPrint(console, kx_soil_recount)
    else:
        kx_soil_recount = kx_soil_modified

    print(kx_soil_recount)

    for i in range(0, len(L)):
        elem = np.append(elem, i).astype(int)

    dbgPrint(console, 'Počet navržených elementů: ' + str(len(elem)))
    # Délky jednotlivých prvků Vše přeložit do ajiny nakonec jako vždy
    q = 0.
    n0 = 0.

    # uzly souřadnice pro prvky?
    nodes = np.array([])

    for i in range(0, len(L)):
        nodes = np.append(nodes, np.sum(L[:i]))
        nodes = np.append(nodes, np.sum(L[:(i + 1)]))

    # pro výpočet normálovek etc.
    nodes1 = np.array([])
    for i in range(0, len(L) + 1):
        nodes1 = np.append(nodes1, np.sum(L[:i]))

    nodes2 = np.array([])
    for i in range(0, len(L)):
        nodes2 = np.append(nodes2, np.sum(L[:i]))
    # split na počet prvků!!!
    mid_nodes = np.array_split(nodes, len(elem))
    mid_nodes_ = np.array([])
    for i in range(0, len(mid_nodes)):
        _a = (mid_nodes[i][0] + mid_nodes[i][1]) / 2
        mid_nodes_ = np.append(mid_nodes_, _a)

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
        II = [i * 3, i * 3, i * 3, i * 3, i * 3, i * 3, i * 3 + 1, i * 3 + 1, i * 3 + 1, i * 3 + 1, i * 3 + 1,
              i * 3 + 1, i * 3 + 2, i * 3 + 2, i * 3 + 2, i * 3 + 2, i * 3 + 2, i * 3 + 2, i * 3 + 3, i * 3 + 3,
              i * 3 + 3, i * 3 + 3, i * 3 + 3, i * 3 + 3, i * 3 + 4, i * 3 + 4, i * 3 + 4, i * 3 + 4, i * 3 + 4,
              i * 3 + 4, i * 3 + 5, i * 3 + 5, i * 3 + 5, i * 3 + 5, i * 3 + 5, i * 3 + 5]
        I = np.append(I, II)
        JJ = [i * 3, i * 3 + 1, i * 3 + 2, i * 3 + 3, i * 3 + 4, i * 3 + 5, i * 3, i * 3 + 1, i * 3 + 2,
              i * 3 + 3, i * 3 + 4, i * 3 + 5, i * 3, i * 3 + 1, i * 3 + 2, i * 3 + 3, i * 3 + 4, i * 3 + 5, i * 3,
              i * 3 + 1, i * 3 + 2, i * 3 + 3, i * 3 + 4, i * 3 + 5, i * 3, i * 3 + 1, i * 3 + 2, i * 3 + 3, i * 3 + 4,
              i * 3 + 5, i * 3, i * 3 + 1, i * 3 + 2, i * 3 + 3, i * 3 + 4, i * 3 + 5]
        J = np.append(J, JJ)
        KK = [edpile[i] * apile[i] / L[i] + ky_soil_modified[i] * L[i] / 3, 0, 0, -edpile[i] * apile[i] / L[i] + ky_soil_modified[i] * L[i] / 6, 0, 0, 0,
              12 * (edpile[i] * Jypile[i]) / L[i] ** 3 + (156 / 420) * kx_soil_recount[i] * L[i],
              6 * (edpile[i] * Jypile[i]) / L[i] ** 2 + (22 / 420) * kx_soil_recount[i] * L[i] ** 2, 0,
              -12 * (edpile[i] * Jypile[i]) / L[i] ** 3 + (54 / 420) * kx_soil_recount[i] * L[i],
              6 * (edpile[i] * Jypile[i]) / L[i] ** 2 - (13 / 420) * kx_soil_recount[i] * L[i] ** 2, 0,
              6 * (edpile[i] * Jypile[i]) / L[i] ** 2 + (22 / 420) * kx_soil_recount[i] * L[i] ** 2,
              4 * (edpile[i] * Jypile[i]) / L[i] + (4 / 420) * kx_soil_recount[i] * L[i] ** 3, 0,
              -6 * (edpile[i] * Jypile[i]) / L[i] ** 2 + (13 / 420) * kx_soil_recount[i] * L[i] ** 2,
              2 * (edpile[i] * Jypile[i]) / L[i] - (3 / 420) * kx_soil_recount[i] * L[i] ** 3,
              -edpile[i] * apile[i] / L[i] + ky_soil_modified[i] * L[i] / 6, 0, 0, edpile[i] * apile[i] / L[i] + ky_soil_modified[i] * L[i] / 3, 0, 0, 0,
              -12 * (edpile[i] * Jypile[i]) / L[i] ** 3 + (54 / 420) * kx_soil_recount[i] * L[i],
              -6 * (edpile[i] * Jypile[i]) / L[i] ** 2 + (13 / 420) * kx_soil_recount[i] * L[i] ** 2, 0,
              12 * (edpile[i] * Jypile[i]) / L[i] ** 3 + (156 / 420) * kx_soil_recount[i] * L[i],
              -6 * (edpile[i] * Jypile[i]) / L[i] ** 2 - (22 / 420) * kx_soil_recount[i] * L[i] ** 2, 0,
              6 * (edpile[i] * Jypile[i]) / L[i] ** 2 - (13 / 420) * kx_soil_recount[i] * L[i] ** 2,
              2 * (edpile[i] * Jypile[i]) / L[i] - (3 / 420) * kx_soil_recount[i] * L[i] ** 3, 0,
              -6 * (edpile[i] * Jypile[i]) / L[i] ** 2 - (22 / 420) * kx_soil_recount[i] * L[i] ** 2,
              4 * (edpile[i] * Jypile[i]) / L[i] + (4 / 420) * kx_soil_recount[i] * L[i] ** 3]
        K = np.append(K, KK)
        # K = np.append(K,
        #               [(E * A / L[i] + kx * L[i] / 3), 0., 0, -E * A / L[i] + kx * L[i] / 6, 0, 0, 0,
        #                12 * (E * I_y + ky) / L[i] ** 3,
        #                6 * (E * I_y + ky) / L[i] ** 2, 0,
        #                -12 * (E * I_y + ky) / L[i] ** 3,
        #                6 * (E * I_y + ky) / L[i] ** 2, 0,
        #                6 * (E * I_y + ky) / L[i] ** 2, 4 * (E * I_y + ky) / L[i], 0,
        #                -6 * (E * I_y + ky) / L[i] ** 2, 2 * (E * I_y + ky) / L[i], -E * A / L[i] + kx * L[i] / 6, 0, 0,
        #                E * A / L[i] + kx * L[i] / 3, 0, 0, 0,
        #                -12 * (E * I_y + ky) / L[i] ** 3, -6 * (E * I_y + ky) / L[i] ** 2, 0,
        #                12 * (E * I_y + ky) / L[i] ** 3,
        #                -6 * (E * I_y + ky) / L[i] ** 2, 0, 6 * (E * I_y + ky) / L[i] ** 2,
        #                2 * (E * I_y + ky) / L[i], 0, -6 * (E * I_y + ky) / L[i] ** 2,
        #                4 * (E * I_y + ky) / L[i]])
        fij = np.append(fij, [i * 3, i * 3 + 1, i * 3 + 2, i * 3 + 3, i * 3 + 4, i * 3 + 5])
        f = np.append(f, [0.5 * n0 * L[i], (1 / 2) * q * L[i], (1 / 12) * q * L[i] ** 2, 0.5 * n0 * L[i],
                          (1 / 2) * q * L[i], (-1 / 12) * q * L[i] ** 2])

    I = I.astype(int)
    J = J.astype(int)
    fij = fij.astype(int)

    K_glob = np.zeros(((len(elem) + 1) * 3, (len(elem) + 1) * 3))
    for i in range(0, len(K)):
        K_glob[I[i], J[i]] += K[i]

    # K_glob = coo_matrix((K, (I, J))).tolil()
    # print(K_glob)

    f_glob = np.zeros(((len(elem) + 1) * 3, (len(elem) + 1) * 3))
    for i in range(0, len(f)):
        f_glob[fij[i], fij[i]] += f[i]
    # f_glob1 = coo_matrix((f, (fij, fij))).tolil()
    # print(f_glob1.toarray().astype(int))
    # sys.exit("Test matic")

    f_glob_i, f_glob_j = f_glob.shape

    f_glob_vec = np.array([])
    for i in range(f_glob_i):
        for j in range(f_glob_j):
            if i == j:
                f_glob_vec = np.append(f_glob_vec, f_glob[i, j])

    # end node normal point placement
    end_normal_node = len(elem) * 3

    # Foot spring stiffnes
    K_glob[end_normal_node, end_normal_node] += ky_foot

    if BC == 1:
        print('BC1')
        pass
    elif BC == 2:
        K_glob[end_normal_node, :] = 0
        K_glob[:, end_normal_node] = 0
        K_glob[end_normal_node, end_normal_node] = 1

        f_glob_vec[end_normal_node] = 0
        print('BC2')
    else:
        K_glob[end_normal_node, :] = 0
        K_glob[:, end_normal_node] = 0
        K_glob[end_normal_node, end_normal_node] = 1

        K_glob[:, end_normal_node+1] = 0
        K_glob[end_normal_node+1, :] = 0
        K_glob[end_normal_node+1, end_normal_node+1] = 1

        f_glob_vec[end_normal_node] = 0
        f_glob_vec[end_normal_node+1] = 0
        print('BC3')

    """
    end_boundary = len(elem)*3 + 1
    print(end_boundary)
    print('_____')
    K_glob[:, end_boundary] = 0
    K_glob[end_boundary, :] = 0
    K_glob[end_boundary, end_boundary] = 1
    """

    # setting up forces at top of pile
    f_glob_vec[0] += float(ver_force)
    f_glob_vec[1] += float(hor_force)
    f_glob_vec[2] += float(bend_force)
    # [15] = 0.5
    try:
        u = np.linalg.solve(K_glob, f_glob_vec)
    except np.linalg.LinAlgError:
        dbgPrint(console, 'Matice je singulární!')
        return None

    # 11BS znamená počet dělení, kolik je uzlů na modelu!!
    uu = np.array_split(u, len(nodes1))
    M = np.array([])
    V = np.array([])
    N = np.array([])
    U_horizontal = np.array([])

    U_vertical = np.array([])

    for i in elem:
        n_1 = uu[i][0]
        v_1 = uu[i][1]
        w_1 = uu[i][2]
        n_2 = uu[i + 1][0]
        v_2 = uu[i + 1][1]
        w_2 = uu[i + 1][2]

        U_horizontal = np.append(U_horizontal, uu[i][1])
        U_horizontal = np.append(U_horizontal, uu[i+1][1])

        U_vertical= np.append(U_vertical, uu[i][0])
        U_vertical = np.append(U_vertical, uu[i + 1][0])

        M0 = -edpile[i] * Jypile[i] * (
        v_1 * (-6 / L[i] ** 2) + w_1 * (-4 / L[i]) + v_2 * (6 / L[i] ** 2) + w_2 * (-2 / L[i]))
        M = np.append(M, M0)
        ML = -edpile[i] * Jypile[i] * (
            v_1 * (((12 * L[i]) / L[i] ** 3) - (6 / L[i] ** 2)) + w_1 * ((6 * L[i] / L[i] ** 2) - (4 / L[i])) + v_2 * (
                (6 / L[i] ** 2) - (12 * L[i] / L[i] ** 3)) + w_2 * ((6 * L[i] / L[i] ** 2) - (2 / L[i])))
        M = np.append(M, ML)
        VL = -edpile[i] * Jypile[i] * (
        v_1 * 12 / L[i] ** 3 + w_1 * 6 / L[i] ** 2 - v_2 * 12 / L[i] ** 3 + w_2 * 6 / L[i] ** 2)
        V = np.append(V, VL)
        NL = ((edpile[i] * apile[i]) / L[i]) * (n_2 - n_1)
        N = np.append(N, NL)

    dbgPrint(console, 'Momenty:')
    dbgPrint(console, M)
    dbgPrint(console, 'Posouvající síly: ')
    dbgPrint(console, V)
    dbgPrint(console, 'Normálové síly: ')
    dbgPrint(console, N)

    nodesplus = np.array([])
    nodesminus = np.array([])
    lplus = np.array([])
    vplus = np.array([])
    vminus = np.array([])
    lminus = np.array([])

    for i in range(0, len(V)):
        if V[i] >= 0:
            nodesplus = np.append(nodesplus, nodes2[i])
            vplus = np.append(vplus, V[i])
            lplus = np.append(lplus, L[i])
        else:
            nodesminus = np.append(nodesminus, nodes2[i])
            vminus = np.append(vminus, V[i])
            lminus = np.append(lminus, L[i])

    fig, ax1 = plt.subplots()

    ax1.set_xlabel(r'$L[m]$')
    ax1.set_ylabel(r'$u_x[m]$')
    plt.title(r'Horizontal displacement Ux')

    ax1.fill_between(nodes, 0, U_horizontal, facecolor='none',  edgecolor='b')

    ax1.legend(['Ux', 'Ux-'], loc='upper right')
        # Can invert axis by default
        # ax1.invert_yaxis()

    plt.axhline(0, color='black')
    fig.savefig('výsledky/Ux.png', bbox_inches='tight')
    plt.close()
    plt.clf()

    fig, ax1 = plt.subplots()

    ax1.set_xlabel(r'$L[m]$')
    ax1.set_ylabel(r'$u_x[m]$')
    plt.title(r'Vertical displacement Uy')

    ax1.fill_between(nodes, 0, U_vertical, facecolor='none', edgecolor='b')

    ax1.legend(['Uy', 'Ux-'], loc='upper right')
    # Can invert axis by default
    # ax1.invert_yaxis()

    plt.axhline(0, color='black')
    fig.savefig('výsledky/Uy.png', bbox_inches='tight')
    plt.close()
    plt.clf()

    try:
        fig, ax1 = plt.subplots()

        ax1.set_xlabel(r'$L[m]$')
        ax1.set_ylabel(r'$M[Nm]$')
        plt.title(r'Internal force M')

        ax1.fill_between(nodes, 0, M, facecolor='none', where=M >= 0, hatch='|', edgecolor='b', interpolate=True)
        ax1.fill_between(nodes, 0, M, facecolor='none', where=0 >= M, hatch='|', edgecolor='r', interpolate=True)

        legend1 = plt.Rectangle((0, 0), 1, 1, fc='none', hatch='|', edgecolor='b')
        legend2 = plt.Rectangle((0, 0), 1, 1, fc='none', hatch='|', edgecolor='r')

        ax1.legend([legend1, legend2], ['M+', 'M-'], loc='upper right')
        # Can invert axis by default
        # ax1.invert_yaxis()
        """
        for i, j in zip(nodes, M):
            ax1.annotate(str(int(j)), xy=(i, j), rotation=90)
        """
        plt.axhline(0, color='black')
        fig.savefig('výsledky/M.png', bbox_inches='tight')
        plt.close()
        plt.clf()
    except:
        dbgPrint(console, 'Chyba tisku momentů, pravděpodobně nulové momenty?')
        dbgPrint(console, 'Neočekáváná chyba: ' + str(sys.exc_info()[0]))

    # Nový graf V
    try:
        fig, ax1 = plt.subplots()

        ax1.set_xlabel(r'$L[m]$')
        ax1.set_ylabel(r'$V[N]$')
        plt.title(r'Internal force V')

        if len(vplus) > 0:
            ax1.bar(nodesplus, vplus, lplus, color=(0, 0, 0, 0), edgecolor='b', )
        if len(vminus) > 0:
            ax1.bar(nodesminus, vminus, lminus, color=(0, 0, 0, 0), edgecolor='r', )
        """
        for i, j in zip(nodesplus, vplus):
            ax1.annotate(str(int(j)), xy=(i, j), rotation=90)
        for i, j in zip(nodesplus, vplus):
            ax1.annotate(str(int(j)), xy=(i, j), rotation=90)
        """
        legend1 = plt.Rectangle((0, 0), 1, 1, fc='none', hatch='|', edgecolor='b')
        legend2 = plt.Rectangle((0, 0), 1, 1, fc='none', hatch='|', edgecolor='r')

        ax1.legend([legend1, legend2],['V+', 'V-'], loc='upper right')

        plt.axhline(0, color='black')
        fig.savefig('výsledky/V.png', bbox_inches='tight')
        plt.close()
        plt.clf()
    except:
        dbgPrint(console, 'Chyba tisku smykových sil, pravděpodobně nulové smykové síly?')
        dbgPrint(console, 'Neočekáváná chyba: ' + str(sys.exc_info()[0]))

    # Nový graf N
    try:
        fig, ax1 = plt.subplots()

        ax1.set_xlabel(r'$L[m]$')
        ax1.set_ylabel(r'$N[N]$')
        plt.title(r'Internal force N')

        ax1.bar(nodes2, N, L, color=(0, 0, 0, 0), edgecolor='b', )  # Normálovky

        ax1.legend(['N+', 'N-'], loc='upper right')

        plt.axhline(0, color='black')
        fig.savefig('výsledky/N.png', bbox_inches='tight')
        plt.close()
        plt.clf()
    except:
        dbgPrint(console, 'Chyba tisku normálových sil, pravděpodobně nulové normálové síly?')
        dbgPrint(console, 'Neočekáváná chyba: ' + str(sys.exc_info()[0]))

    dbgPrint(console, '|--------------------------------------|')
    dbgPrint(console, '(------KONEC VÝPOČTU MKP------)')
    dbgPrint(console, '|--------------------------------------|')
