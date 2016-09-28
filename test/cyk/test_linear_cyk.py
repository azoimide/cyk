from cnf import read_linear_grammar
from cyk import linear_cyk
from util import map_string

def test():

    with open('grammar_lin.txt', 'r') as f:
        lnups, rnups, ups, nt_tab, t_tab, start = read_linear_grammar(f)

    s1 = map_string("abc",t_tab)
    s2 = map_string("abca",t_tab)
    
    assert linear_cyk(lnups, rnups, ups, s1, debug=False)
    assert not linear_cyk(lnups, rnups, ups, s2, debug=False)

if __name__ == "__main__":
    test()
