from util import print_arr

UNDEF = 0
DERIVES = 1
NOT_DERIVES = 2

def linear_cyk(lnups, rnups, ups, s, tab=None, N=0, i=None, j=None, naive=False, debug=False):

    # Initialization for root recursive call
    if not naive and tab == None:
        tab = [ [ [ UNDEF for k in range(len(rnups)) ] for _ in range(len(s)) ] for _ in range(len(s)) ]
    if i == None:
        i = 0
    if j == None:
        j = len(s) - 1

    # Already solved for given substring and non-terminal
    if not naive and tab[i][j][N] != UNDEF:
        return tab[i][j][N] == DERIVES

    elif i == j:

        # Attempt unit production derivation (N -> T)
        for up in ups[N]:
            if up == s[i]:
                if debug:
                    print "i:", i, "j:", j, "N:", N, "True"
                if not naive:
                    tab[i][j][N] = DERIVES
                    if debug:
                        print_arr(tab)
                return True

        # No matching unit production
        if debug:
            print "i:", i, "j:", j, "N:", N, "False"
        if not naive:
            tab[i][j][N] = NOT_DERIVES
            if debug:
                print_arr(tab)
        return False

    else:

        # Attempt left linear derivation (N -> NT)
        for lnup in lnups[N]:
            if s[j] == lnup[1] and linear_cyk(lnups, rnups, ups, s, tab, lnup[0], i, j - 1, naive=naive, debug=debug):
                if debug:
                    print "i:", i, "j:", j, "N:", N, "True"
                if not naive:
                    tab[i][j][N] = DERIVES
                    if debug:
                        print_arr(tab)
                return True

        # Attempt right linear derivation (N -> TN)
        for rnup in rnups[N]:
            if s[i] == rnup[0] and linear_cyk(lnups, rnups, ups, s, tab, rnup[1], i + 1, j, naive=naive, debug=debug):
                if debug:
                    print "i:", i, "j:", j, "N:", N, "True"
                if not naive:
                    tab[i][j][N] = DERIVES
                    if debug:
                        print_arr(tab)
                return True

        # i != j, no derivation found
        if debug:
            print "i:", i, "j:", j, "N:", N, "False"
        if not naive:
            tab[i][j][N] = NOT_DERIVES
            if debug:
                print_arr(tab)
        return False
