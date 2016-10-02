from cnf import read_grammar
from self_correcting_cyk import self_correcting_cyk
from util import map_string

def a_n_b_n():
    with open("a_n_b_n.txt", "r") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s = "aabb"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = "bbaa"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = "abbb"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = "abbbb"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = "bbab"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

def sci_not():
    with open("sci_not.txt", "r") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s = "+.e-0"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = "++e-0"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = "1+e-0"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = "1+e-"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

def brackets():
    with open("brackets.txt", "r") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s = "()"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = ")("
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = "())"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = "()()))"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = "()))()"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = "))))))"
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

    s = "()()()("
    assert [] == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[1]

def main():
    a_n_b_n()
    sci_not()
    brackets()

if __name__ == "__main__":
    main()
