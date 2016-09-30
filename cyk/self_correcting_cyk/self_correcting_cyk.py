from util import print_arr

def self_correcting_cyk(nups, ups, s, start=0, debug=False):
    l = len(s)
    tab = [ [ [len(s) + 1 for k in range(len(nups)) ] for i in range(l) ] for j in range(l) ]
    inf = len(s) + 1

    # Set [0,c,N] to 1 if N is LHS in at least one unit production,
    # set [0,c,N] to 0 if N produces s[c]
    for c in range(l):
        for n in range(len(ups)):
            if len(ups[n]) > 0:
                tab[0][c][n] = 1
                for up in ups[n]:
                    if up == s[c]:
                        tab[0][c][n] = 0
                        break

    # For each non-terminal and substring, find the cheapest split
    for r in range(1, l):
        if debug:
            print_arr(tab)
        for c in range(r, l):
            for n in range(len(nups)):
                minn = inf
                for k in range(1, r + 1):
                    for nup in nups[n]:
                        cost = tab[r - k][c - k][nup[0]] + tab[k - 1][c][nup[1]]
                        if cost < minn:
                            minn = cost
                tab[r][c][n] = minn

    if debug:
        print_arr(tab)

    return (tab[-1][-1][start], [])



def self_correcting_cyk2(nups, ups, s, start=0, debug=False):
    l = len(s)
    tab = [ [ [len(s) + 1 for k in range(len(nups)) ] for i in range(l) ] for j in range(l) ]
    inf = len(s) + 1

    # Set [0,c,N] to 1 if N is LHS in at least one unit production,
    # set [0,c,N] to 0 if N produces s[c]
    for c in range(l):
        for n in range(len(ups)):
            if len(ups[n]) > 0:
                # tab[0][c][n] = 1
                for up in ups[n]:
                    if up == s[c]:
                        tab[0][c][n] = 0
                        break

    # For each non-terminal and substring, find the cheapest split
    for r in range(1, l):
        # if debug:
        #     print_arr(tab)
        for c in range(r, l):
            for n in range(len(nups)):
                minn = inf
                for k in range(1, r + 1):
                    for nup in nups[n]:
                        cost = tab[r - k][c - k][nup[0]] + tab[k - 1][c][nup[1]]
                        if cost < minn:
                            minn = cost
                if tab[r - 1][c][n] + 1 < minn:
                    minn = tab[r - 1][c][n] + 1
                if tab[r - 1][c - 1][n] + 1 < minn:
                    minn = tab[r - 1][c - 1][n] + 1
                tab[r][c][n] = minn

    if debug:
        print_arr(tab)

    return (tab[-1][-1][start], [])

