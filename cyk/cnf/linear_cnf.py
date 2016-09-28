import sys

def read_linear_grammar(f=sys.stdin):
    lines = f.readlines()
    # rule_lines = lines[:-1]
    rule_lines = lines
    # s = map(lambda c: ord(c) - ord('a'), lines[-1].strip())
    ups = []
    rnups = []
    lnups = []
    nt_count = 0
    t_count = 0
    t_tab = {}
    nt_tab = {}
    for line in rule_lines:
        if line[0] == '#':
            continue
        lhs, rhs = line.strip().split(' ')

        # New N in LHS
        if lhs not in nt_tab:
            nt_tab[lhs] = len(nt_tab)
            lnups.append([])
            rnups.append([])
            ups.append([])

        # N -> T (up)
        if len(rhs) == 1: 
            if rhs.istitle():
                raise ValueError("Invalid terminal: " + rhs)
            if rhs not in t_tab:
                t_tab[rhs] = len(t_tab)
            ups[nt_tab[lhs]].append(t_tab[rhs])
        else:

            # N -> NT (lnup)
            if rhs[0].istitle() and not rhs[1].istitle(): 
                nt = rhs[0]
                t = rhs[1]

                # New N in RHS
                if nt not in nt_tab:
                    nt_tab[nt] = len(nt_tab)
                    ups.append([])
                    rnups.append([])
                    lnups.append([])

                # New T in RHS
                if t not in t_tab:
                    t_tab[t] = len(t_tab)

                lnups[nt_tab[lhs]].append((nt_tab[nt],t_tab[t]))

            # N -> TN (rnup)
            elif not rhs[0].istitle() and rhs[1].istitle(): 
                t = rhs[0]
                nt = rhs[1]

                # New N in RHS
                if nt not in nt_tab:
                    nt_tab[nt] = len(nt_tab)
                    ups.append([])
                    rnups.append([])
                    lnups.append([])

                # New T in RHS
                if t not in t_tab:
                    t_tab[t] = len(t_tab)

                rnups[nt_tab[lhs]].append((t_tab[t],nt_tab[nt]))
            else:
                raise ValueError("Invalid rule: " + line)
    return lnups, rnups, ups, nt_tab, t_tab, 0

