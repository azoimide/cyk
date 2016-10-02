from cnf import read_grammar
from self_correcting_cyk import self_correcting_cyk
from util import map_string

def a_n_b_n():
    with open("a_n_b_n.txt", "r") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s = "aabb"
    assert 0 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "bbaa"
    assert 3 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "abbb"
    assert 1 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "abbbb"
    assert 2 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "bbab"
    assert 2 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

def sci_not():
    with open("sci_not.txt", "r") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s = "+.e-0"
    assert 0 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "++e-0"
    assert 1 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "1+e-0"
    assert 2 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "1+e-"
    assert len(s) < self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "11+.1e-0"
    assert 2 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "1+0.01e-0"
    assert 1 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "01+.e0-1110"
    assert 3 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "+11.1001e-101010"
    assert 0 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

def brackets():
    with open("brackets.txt", "r") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s = "()"
    assert 0 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = ")("
    assert 2 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "())"
    assert 1 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "()()))"
    assert 1 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "()))()"
    assert 1 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "))))))"
    assert 3 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

    s = "()()()("
    assert 1 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True, change=True)[0]

def main():
    a_n_b_n()
    sci_not()
    brackets()

if __name__ == "__main__":
    main()
