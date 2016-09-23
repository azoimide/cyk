from cnf import read_grammar
from cyk import cyk_td
from util import map_string

def test():
    # s = [2, 0, 1]
    # s = [2, 0, 0, 1]
    # print s

    with open('grammar_cnf.txt', 'r') as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s = map_string("abc",t_tab)

    # print "nt_tab:", nt_tab
    # print "t_tab:", t_tab
    # print "nups:", nups
    # print "ups:", ups
    # print "rev_ups:", rev_ups
    
    assert cyk_td(nups, ups, s)

if __name__ == "__main__":
    test()
