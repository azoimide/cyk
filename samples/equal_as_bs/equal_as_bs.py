from cyk.cyk import cyk_td
from cyk.cnf import read_grammar

if __name__ == "__main__":
    with open("equal_as_bs.txt") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)
    print nt_tab
    s1 = "ababaa"
    s2 = "ab"
    print 's1: "{}", accepted: {}'.format(s1, cyk_td(nups, ups, s1))
    print 's2: "{}", accepted: {}'.format(s2, cyk_td(nups, ups, s2, debug=True))
