from util import print_arr

def cyk_bu(nups, rev_ups, s, start=0, debug=False):
    l = len(s)
    tab = [ [ [0 for k in range(len(nups)) ] for i in range(l) ] for j in range(l) ]

    for c in range(l):
        for up in rev_ups[s[c]]:
            tab[0][c][up] = 1

    for r in range(1, l):
        if debug:
            print_arr(tab)
        for c in range(r, l):
            for k in range(1, r + 1):
                for nt in range(len(nups)):
                    for nup in nups[nt]:
                        if tab[r - k][c - k][nup[0]] and tab[k - 1][c][nup[1]]:
                            tab[r][c][nt] = 1

    if debug:
        print_arr(tab)

    return tab[-1][-1][start] == 1
