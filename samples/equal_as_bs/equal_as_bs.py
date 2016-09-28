from cyk.cyk import cyk_td
from cyk.cnf import read_grammar
from cyk.util import map_string

if __name__ == "__main__":
    with open("equal_as_bs.txt") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)
    s1 = "ababaa"
    print 's1: "{}", accepted: {}'.format(s1, cyk_td(nups, ups, map_string(s1, t_tab)))
    s2 = "ab"
    print 's2: "{}", accepted: {}'.format(s2, cyk_td(nups, ups, map_string(s2, t_tab)))
