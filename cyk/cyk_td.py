import sys
from time import time
from cnf import read_grammar

def print_arr(a):
    print "\n".join(map(str, a))
    print ""

UNDEF = 0
DERIVES = 1
NOT_DERIVES = 2

# tab = [ [ [UNDEF for k in range(nt_count) ] for i in range(l) ] for j in range(l) ]


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


        
if __name__ == "__main__":
    
    nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar()
    # print data

    # print "nt_tab:", nt_tab
    # print "t_tab:", t_tab
    # print "nups:", nups
    # print "ups:", ups
    # print "rev_ups:", rev_ups


    # s = "()"
    # s = "(()())()"
    # s = map(lambda c: t_tab[c], s)
    # s = rand_string(t_tab, l=5)
    # print s
    # print cyk(nups, rev_ups, s, start, debug=True)
    # print derive(nups, ups, s, N=start)

    c = 100
    for l in range(1, 60):
        total = 0
        maxx = None
        for i in range(c):
            s = rand_string(t_tab, l)
            start_time = time()
            #derive(nups, ups, s, N=start, naive=True)
            #derive(nups, ups, s, N=start)
            cyk(nups, rev_ups, s, start)
            stop_time = time()
            total += stop_time - start_time
            if maxx == None or stop_time - start_time > maxx:
                maxx = stop_time - start_time
        print "{},{},{}".format(l, total / c, maxx)






