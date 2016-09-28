from util import print_arr

def self_correcting_cyk(nups, rev_ups, s, start=0, debug=False):
    l = len(s)
    tab = [ [ [len(s) + 1 for k in range(len(nups)) ] for i in range(l) ] for j in range(l) ]

    for c in range(l):
        for n in range(len(nups)):
            tab[0][c][n] = 1
        for up in rev_ups[s[c]]:
            tab[0][c][up] = 0

    for r in range(1, l):
        if debug:
            print_arr(tab)
        for c in range(r, l):
            for nt in range(len(nups)):
                
                for k in range(1, r + 1):
                    for nup in nups[nt]:
                        if tab[r - k][c - k][nup[0]] and tab[k - 1][c][nup[1]]:
                            tab[r][c][nt] = 1

    if debug:
        print_arr(tab)

    return (tab[-1][-1][start], [])

