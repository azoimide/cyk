from util import print_arr

def print_arr2(a):
    for r in a:
        print map(lambda z: map(lambda c: "{:10}".format(c), z), r)
    print ""

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





def self_correcting_cyk3(nups, ups, s, start=0, debug=False):
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

def build_string(tab2, i=None, j=None, N=0, debug=False):
    if i == None:
        i = len(tab2) - 1
    if j == None:
        j = len(tab2) - 1
    children = tab2[i][j][N]
    if debug:
        print "i:", i, "j:", j, children
    if i == 0:
        return [children[0][2]]

    result = sum([ build_string(tab2, i - c[0], j - c[1], c[2]) for c in children ], [])
    if debug:
        print "result:", result
    return result

def self_correcting_cyk4(nups, ups, s, start=0, debug=False):
    l = len(s)
    tab = [ [ [len(s) + 1 for k in range(len(nups)) ] for i in range(l) ] for j in range(l) ]
    tab2 = [ [ [[] for k in range(len(nups)) ] for i in range(l) ] for j in range(l) ]
    inf = len(s) + 1

    # Set [0,c,N] to 1 if N is LHS in at least one unit production,
    # set [0,c,N] to 0 if N produces s[c]
    for c in range(l):
        for n in range(len(ups)):
            if len(ups[n]) > 0:
                tab[0][c][n] = 1
                tab2[0][c][n] = [(1,0,ups[n][0])]
                for up in ups[n]:
                    if up == s[c]:
                        tab[0][c][n] = 0
                        tab2[0][c][n] = [(1,0,s[c])]
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
                            tab2[r][c][n] = [(k,0,nup[0]),(r - k + 1, r - k + 1,nup[1])]
                if tab[r - 1][c][n] + 1 < minn:
                    minn = tab[r - 1][c][n] + 1
                    tab2[r][c][n] = [(1,0,n)]
                if tab[r - 1][c - 1][n] + 1 < minn:
                    minn = tab[r - 1][c - 1][n] + 1
                    tab2[r][c][n] = [(1,1,n)]
                tab[r][c][n] = minn

    if debug:
        print_arr(tab)

    s_fixed = build_string(tab2)

    if tab[-1][-1][start] == 0:
        return (0, s)
    else:
        return (tab[-1][-1][start], s_fixed)


def self_correcting_cyk_all(nups, ups, s, start=0, debug=False, change=False, delete=False):
    l = len(s)
    cost_tab = [ [ [len(s) + 1 for k in range(len(nups)) ] for i in range(l) ] for j in range(l) ]
    str_tab = [ [ [[] for k in range(len(nups)) ] for i in range(l) ] for j in range(l) ]
    inf = len(s) + 1

    # Set [0,c,N] to 1 if N is LHS in at least one unit production,
    # set [0,c,N] to 0 if N produces s[c]
    for c in range(l):
        for n in range(len(ups)):
            if len(ups[n]) > 0:
                if change:
                    cost_tab[0][c][n] = 1
                str_tab[0][c][n] = [(1,0,ups[n][0])]
                for up in ups[n]:
                    if up == s[c]:
                        cost_tab[0][c][n] = 0
                        str_tab[0][c][n] = [(1,0,s[c])]
                        break

    # For each non-terminal and substring, find the cheapest split
    for r in range(1, l):
        if debug:
            print_arr(cost_tab)
        for c in range(r, l):
            for n in range(len(nups)):
                minn = inf
                for k in range(1, r + 1):
                    for nup in nups[n]:
                        cost = cost_tab[r - k][c - k][nup[0]] + cost_tab[k - 1][c][nup[1]]
                        if cost < minn:
                            minn = cost
                            str_tab[r][c][n] = [(k,0,nup[0]),(r - k + 1, r - k + 1,nup[1])]
                if delete:
                    if cost_tab[r - 1][c][n] + 1 < minn:
                        minn = cost_tab[r - 1][c][n] + 1
                        str_tab[r][c][n] = [(1,0,n)]
                    if cost_tab[r - 1][c - 1][n] + 1 < minn:
                        minn = cost_tab[r - 1][c - 1][n] + 1
                        str_tab[r][c][n] = [(1,1,n)]
                cost_tab[r][c][n] = minn

    s_fixed = build_string(str_tab)
    if debug:
        print_arr(cost_tab)

    return (cost_tab[-1][-1][start], s_fixed)




