from cnf import read_grammar
from cyk import cyk_td
from util import map_string

def test():
    with open('grammar_cnf.txt', 'r') as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s = map_string("abc",t_tab)    
    assert cyk_td(nups, ups, s)


    with open('equal_as_bs.txt', 'r') as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s1 = map_string("ababaa",t_tab)
    assert not cyk_td(nups, ups, s1)

    s1 = map_string("ababab",t_tab)
    assert cyk_td(nups, ups, s1)

if __name__ == "__main__":
    test()
