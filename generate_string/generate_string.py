import sys
import random
from cnf import read_grammar
from util import print_arr

def rand_string(t_count, l=10):
    r = Random()
    return [ r.randint(0, t_count - 1) for i in range(l) ]

def generate_table(nups, ups, start, length, debug=False):
    tab = [ [0 for _ in range(length) ] for _ in range(len(nups)) ]
    if debug:
        print_arr(tab)

    # Set true for all non-terminals that appear as LHS of unit productions
    for n in range(len(ups)):
        if len(ups[n]) > 0:
            tab[n][0] = 1

    if debug:
        print_arr(tab)

    for l in range(1, length + 1):
        for k in range(1, l):
            if debug:
                print "l:", l, "k:", k, "l - k:", l - k
            for n in range(len(nups)):
                for nup in nups[n]:
                    if debug:
                        print "nup:", n, "->", nup
                    if tab[nup[0]][k - 1] and tab[nup[1]][l - k - 1]:
                        tab[n][l - 1] = 1
        if debug:
            print_arr(tab)
    
    return tab

def generate_string(nups, ups, tab=None, N=0, s=None, i=None, j=None, length=None, debug=False):

    # Generates table if None and length provided
    if tab is None and not length is None:
        tab = generate_table(nups, ups, N, length)
    if not tab is None and not length is None and length != len(tab[0]):
        raise ValueError("Table of length {} doesn't match specified length {}".format(len(tab[0]), length))

    # Initialization of root recursive call
    if i is None:
        i = 0
    if j is None:
        j = len(tab[0]) - 1
    if s is None:
        s = [ None ] * (j + 1)

    if debug:
        print "\nGENERATE_STRING: N:", N, "i:", i, "j:", j

    # Substring of length 1, choose LHS of random unit production (N -> T)
    if i == j:
        s[i] = random.choice(ups[N])
        if debug:
            print "t:", s[i]
        # Return value only used when returned from root of recursion
        return s

    # Substring longer than one, find all splits that can generate a string
    choices = []
    for nup in nups[N]:
        if debug:
            print "nup:", N, "->", nup

        # Find all possible splits
        for j1 in range(i, j):
            i2 = j1 + 1
            if debug:
                print "j1:", j1, "i2:", i2

            # If the split can generate a string, keep it for random
            if tab[nup[0]][j1 - i] and tab[nup[1]][j - i2]:
                if debug:
                    print "choice:", ((nup[0], j1),(nup[1], i2))
                choices.append(((nup[0], j1),(nup[1], i2)))

    # Randomize split and generate substrings
    (n1, j1), (n2, i2) = random.choice(choices)
    if debug:
        print "n1:", n1, "j1:", j1, "n2:", n2, "i2:", i2
    generate_string(nups, ups, tab, n1, s, i, j1)
    generate_string(nups, ups, tab, n2, s, i2, j)

    # Return value only used when returned from root of recursion
    return s


