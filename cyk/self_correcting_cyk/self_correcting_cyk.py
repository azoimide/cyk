from util import print_arr

def print_arr2(a):
    for r in a:
        print map(lambda z: map(lambda c: "{:10}".format(c), z), r)
    print ""


def self_correcting_cyk(nups, ups, s, start=0, debug=False, change=False, delete=False):
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
                str_tab[0][c][n] = [ups[n][0]]
                for up in ups[n]:
                    if up == s[c]:
                        cost_tab[0][c][n] = 0
                        str_tab[0][c][n] = [s[c]]
                        break

    # For each non-terminal and substring, find the cheapest split
    for r in range(1, l):
        for c in range(r, l):
            for n in range(len(nups)):
                minn = inf
                for k in range(1, r + 1):
                    for nup in nups[n]:
                        cost = cost_tab[r - k][c - k][nup[0]] + cost_tab[k - 1][c][nup[1]]
                        if cost < minn:
                            minn = cost
                            str_tab[r][c][n] = [(k,k,nup[0]),(r - k + 1, 0,nup[1])]
                if delete:
                    if cost_tab[r - 1][c][n] + 1 < minn:
                        minn = cost_tab[r - 1][c][n] + 1
                        str_tab[r][c][n] = [(1,0,n)]
                    if cost_tab[r - 1][c - 1][n] + 1 < minn:
                        minn = cost_tab[r - 1][c - 1][n] + 1
                        str_tab[r][c][n] = [(1,1,n)]
                cost_tab[r][c][n] = minn

    if debug:
        print_arr(cost_tab)
    if (not change and not delete) or cost_tab[-1][-1][start] > len(s):
        s_fixed = []
    else:
        s_fixed = build_string(str_tab, debug=debug)
    
    if debug:
        print "result:", (cost_tab[-1][-1][start], s_fixed)

    return (cost_tab[-1][-1][start], s_fixed)

def build_string(tab2, r=None, c=None, N=0, debug=False):
    if r == None:
        r = len(tab2) - 1
    if c == None:
        c = len(tab2) - 1
    children = tab2[r][c][N]
    if r == 0:
        result = children
    else:
        result = sum([ build_string(tab2, r - child[0], c - child[1], child[2], debug=debug) for child in children ], [])

    if debug:
        print "r:", r, "c:", c, "N:", N, children
        print "result:", result
    return result




