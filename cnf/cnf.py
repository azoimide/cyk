import sys

def read_grammar(f=sys.stdin):
    lines = f.readlines()
    # rule_lines = lines[:-1]
    rule_lines = lines
    # s = map(lambda c: ord(c) - ord('a'), lines[-1].strip())
    ups = []
    nups = []
    rev_ups = []
    nt_count = 0
    t_count = 0
    t_tab = {}
    nt_tab = {}
    for line in rule_lines:
        if line[0] == '#':
            continue
        lhs, rhs = line.strip().split(' ')
        if lhs not in nt_tab:
            nt_tab[lhs] = len(nt_tab)
            nups.append([])
            ups.append([])
        if len(rhs) == 1:
            if rhs not in t_tab:
                t_tab[rhs] = len(t_tab)
                rev_ups.append([])
            ups[nt_tab[lhs]].append(t_tab[rhs])
            rev_ups[t_tab[rhs]].append(nt_tab[lhs])
        else:
            for nt in rhs:
                if nt not in nt_tab:
                    nt_tab[nt] = len(nt_tab)
                    ups.append([])
                    nups.append([])
            nups[nt_tab[lhs]].append(tuple(map(lambda nt: nt_tab[nt], rhs)))
    return nups, ups, rev_ups, nt_tab, t_tab, 0

