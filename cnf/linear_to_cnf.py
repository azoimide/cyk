from copy import deepcopy

def linear_to_cnf(lnups, rnups, ups, nt_tab, t_tab):
    ups = deepcopy(ups)
    nt_tab = deepcopy(nt_tab)
    t_tab = deepcopy(t_tab)
    nups = [ [] for _ in range(len(nt_tab)) ]

    new_rev_ups = [ None for _ in range(len(t_tab)) ]

    for lhs in range(len(lnups)):
        for lnup in lnups[lhs]:
            n1 = lnup[0]
            t = lnup[1]

            n2 = new_rev_ups[t]
            if n2 is None:
                n2 = len(nt_tab)
                new_rev_ups[t] = n2
                nt_tab[n2] = str(n2)
                nups.append([])
                ups.append([])

            nups[lhs].append((n1, n2))

    for lhs in range(len(rnups)):
        for rnup in rnups[lhs]:
            n2 = rnup[1]
            t = rnup[0]

            n1 = new_rev_ups[t]
            if n1 is None:
                n1 = len(nt_tab)
                new_rev_ups[t] = n1
                nt_tab[n1] = str(n1)
                nups.append([])
                ups.append([])

            nups[lhs].append((n1, n2))

    print new_rev_ups
    for i in range(len(new_rev_ups)):
        ups[new_rev_ups[i]].append(i)

    return nups, ups, nt_tab, t_tab


