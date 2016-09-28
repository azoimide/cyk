from util import print_arr

UNDEF = 0
DERIVES = 1
NOT_DERIVES = 2

def cyk_td(nups, ups, s, tab=None, N=0, i=None, j=None, naive=False, debug=False):
    if not naive and tab == None:
        tab = [ [ [UNDEF for k in range(len(nups)) ] for _ in range(len(s)) ] for _ in range(len(s)) ]
    if i == None:
        i = 0
    if j == None:
        j = len(s) - 1

    if debug:
        if not naive:
            print_arr(tab)
        print "i:", i, "j:", j, "N:", N

    if not naive and tab[i][j][N] != UNDEF:
        return tab[i][j][N] == DERIVES

    elif i == j:
        for up in ups[N]:
            if up == s[i]:
                if not naive:
                    tab[i][j][N] = DERIVES
                return True
        if not naive:
            tab[i][j][N] = NOT_DERIVES
        return False

    else:
        for nup in nups[N]:
            for k in range(i, j):
                if cyk_td(nups, ups, s, tab, nup[0], i, k, naive=naive, debug=debug) and \
                   cyk_td(nups, ups, s, tab, nup[1], k + 1, j, naive=naive, debug=debug):
                    if not naive:
                        tab[i][j][N] = DERIVES
                    return True
        if not naive:
            tab[i][j][N] = NOT_DERIVES
        return False
