import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc('font', **{'sans-serif': 'Arial',
                         'family': 'sans-serif'})
import io
import sys


# Never mind this for now
def interpolate_Esi(li, d_pile, soil_type):
    # modify li, so soil is now +-0,000, then count thickness for every layer
    li_modif = np.array([])
    for i in range(0, len(li) - 1):
        li_modif = np.append(li_modif, li[i + 1] - li[i])
    Ed = np.array([])
    return


def dbgPrint(console, *objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    # ignore file, uses StringIO API
    sIO = io.StringIO()
    print(*objects, sep=sep, end=end, file=sIO, flush=flush)
    console.insertPlainText(sIO.getvalue())
    sIO.close()


def masopust(console, L_soil: np.array([]), h_head_pile: float, L_pile: np.array([]), D_pile: np.array([]), reg_a: list,
             reg_b: list, reg_e: list,
             reg_f: list, soil_Es: list, pile_E: np.array([]), m2: np.array([]), V: float, m1=0.7):
    # THIS IS OUR +-0,000m
    starting_pile_height = h_head_pile

    # GETTING HEIGHTS OF PILE SEGMENTS
    L_pile_heights = np.array([0])
    d_pile = np.array([])

    L_soil_heights = np.array([h_head_pile])
    for i in range(0, len(L_pile)):
        L_pile_heights = np.append(L_pile_heights, L_pile[i] + L_pile_heights[i])
        d_pile = np.append(d_pile, D_pile[i])
    for i in range(0, len(L_soil)):
        L_soil_heights = np.append(L_soil_heights, L_soil[i] + L_soil_heights[i])

    # Need to cut overflowing soil under pile
    _t = True
    L_soil_heights_modified = L_soil_heights
    while _t:
        if L_soil_heights_modified[-1] > L_pile_heights[-1]:
            if L_soil_heights_modified[-2] > L_pile_heights[-1]:
                L_soil_heights_modified = np.delete(L_soil_heights, -1, axis=0)
            else:
                L_soil_heights_modified[-1] = L_pile_heights[-1]
        else:
            _t = False

    a = np.array([])
    b = np.array([])
    e = np.array([])
    f = np.array([])

    Di = np.array([])
    li = np.array([])
    Es_mod = np.array([])
    for i in range(0, len(L_soil_heights_modified) - 1):
        Di = np.append(Di, (L_soil_heights_modified[i] + L_soil_heights_modified[i + 1]) / 2)
        li = np.append(li, (L_soil_heights_modified[i + 1] - L_soil_heights_modified[i]))
        a = np.append(a, reg_a[i])
        b = np.append(b, reg_b[i])
        e = np.append(e, reg_e[i])
        f = np.append(f, reg_f[i])
        Es_mod = np.append(Es_mod, soil_Es[i])
    modified_L_pile = np.delete(L_pile_heights, 0, axis=0)

    # Algorithm for appending pile params to soil layers
    modified_d_pile = np.array([])
    modified_m2 = np.array([])
    for i in range(0, len(Di)):
        j = 0
        while modified_L_pile[j] < Di[i]:
            j += 1
        modified_d_pile = np.append(modified_d_pile, d_pile[j])
        modified_m2 = np.append(modified_m2, m2[j])

    # Computing shear
    qsi = np.array([])
    for i in range(0, len(Di)):
        qs = a[i] - b[i] / (Di[i] / modified_d_pile[i])
        qsi = np.append(qsi, qs)

    print(qsi)

    rsu_sum = 0
    qs_sum = 0
    for i in range(0, len(Di)):
        rsu_sum += modified_d_pile[i] * li[i] * qsi[i] * modified_m2[i]
        print(modified_d_pile[i] * li[i] * qsi[i] * modified_m2[i])
        qs_sum += modified_d_pile[i] * li[i]
        print(modified_d_pile[i] * li[i])

    Rsu = m1 * np.pi * rsu_sum

    # Foot bearing
    qp = e[-1] - f[-1] / (L_pile_heights[-1] / modified_d_pile[-1])
    qs_ = rsu_sum / qs_sum

    beta = qp / (qp + (4 * qs_ * L_pile_heights[-1] / modified_d_pile[-1]))

    # Fully loaded shear
    Ry = Rsu / (1 - beta)

    # Implementation of our procedure for achieving vertical displacements
    # interpolate_Esi(L_soil_heights_modified, modified_d_pile, soil_type)
    Es_ = sum(Es_mod * li) / sum(li)
    Ec_ = np.mean(pile_E)
    frac_l_d = L_pile_heights[-1] / (sum(modified_d_pile * li) / sum(li))

    I1 = 0.01075803 + (0.7034923 - 0.01075803) / (1 + (frac_l_d / 1.973465) ** 0.9185353)
    K = Ec_ / Es_

    ld1 = (K + 4.75) / (1.01 * K + 3.24)
    ld2 = (K + 5.01) / (0.99 * K + 2.25)
    ld3 = (K + 19.72) / (K + 9.51)
    ld4 = 0.97 + (4.55 - 0.97) / (1 + (K / 5.0613) ** 0.7866)
    ld5 = 0.98 + (5.4 - 0.98) / (1 + (K / 18.9375) ** 0.8141)
    ld6 = 0.96 + (4.64 - 0.96) / (1 + (K / 102.7411) ** 0.9159)
    ld7 = 0.97 + (4.85 - 0.97) / (1 + (K / 370.7263) ** 1.0196)

    xp = np.array([1, 2, 5, 10, 25, 50, 100])
    yp = np.array([ld1, ld2, ld3, ld4, ld5, ld6, ld7])

    Rk = np.interp(frac_l_d, xp, yp)


    I = I1 * Rk

    sy = I * Ry / ((sum(modified_d_pile * li) / sum(li)) * Es_)

    Rpu = beta * Ry * (25 / sy)
    Rbu = Rsu + Rpu
    print(beta)
    print(Rsu)
    print(Ry)
    print(Rpu)
    print(Rbu)

    our_R = V
    if our_R < Ry:
        our_s = sy * (our_R / Ry) ** 2
    elif our_R <= Rbu:
        our_s = sy + ((25 - sy) / (Rbu - Ry)) * (our_R - Ry)
    else:
        our_s = 0

    # Create output
    fig, ax1 = plt.subplots()

    ax1.set_xlabel(r'$R[kN]$')
    ax1.set_ylabel(r'$s[mm]$')
    plt.title(r'Limitní zatěžovací křivka pro pilotu.')

    x1 = np.arange(0, Ry, 1.)
    y1 = sy * (x1 / Ry) ** 2

    x2 = np.arange(Ry, Rbu, 1.)
    y2 = sy + ((25 - sy) / (Rbu - Ry)) * (x2 - Ry)

    plt.plot(x1, y1, c='b')
    plt.plot(x2, y2, c='r')

    plt.plot([our_R, our_R], [25, our_s], 'k--')
    plt.plot([0, our_R], [our_s, our_s], 'k--')

    ax1.annotate(str(np.round(our_s, 2)) + ' mm', xy=(0, our_s), xytext=(5, 5), xycoords='data',
                 textcoords='offset points')
    ax1.annotate(str(int(our_R)) + ' kN', xy=(our_R, 25), rotation=90, xytext=(5, 45), xycoords='data',
                 textcoords='offset points')

    ax1.legend(['První větev', 'Druhá větev', 'Naše zatížení'], loc='upper right')
    ax1.invert_yaxis()
    plt.figure(figsize=(7.3, 5.7), dpi=96)
    fig.savefig('výsledky/masopust.png')
    plt.close()
    plt.clf()

    dbgPrint(console, 'VÝSLEDKY VÝPOČTU:')
    dbgPrint(console, 'Pro zatížení {0} kN bylo dosaženo sedání {1} mm.'.format(str(np.round(our_R, 2)),
                                                                                str(np.round(our_s, 2))))
    dbgPrint(console,
             'První větev mezní zatěžovací křivky má souřadnice:  zatížení Ry = {0} kN a sedání sy = {1} mm.'.format(
                 str(np.round(Ry, 2)), str(np.round(sy, 2))))
    dbgPrint(console,
             'Druhá větev končí souřadnicemi Rbu = {0} kN při dosažení hraničního sedání 25 mm.'.format(
                 str(np.round(Rbu, 2))))
    return our_s, our_R, Rbu, sy, Ry
