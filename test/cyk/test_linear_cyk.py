from cnf import read_linear_grammar
from cyk import linear_cyk
from util import map_string

def test():
    # s = [2, 1, 0]
    # print s

    with open('grammar_lin.txt', 'r') as f:
        lnups, rnups, ups, nt_tab, t_tab, start = read_linear_grammar(f)

    s = map_string("abc",t_tab)
    
    # print "nt_tab:", nt_tab
    # print "t_tab:", t_tab
    # print "lnups:", lnups
    # print "rnups:", rnups
    # print "ups:", ups
    
    assert linear_cyk(lnups, rnups, ups, s, debug=False)

if __name__ == "__main__":
    test()
