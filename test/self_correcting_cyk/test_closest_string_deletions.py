from cnf import read_grammar
from self_correcting_cyk import self_correcting_cyk
from util import map_string, map_to_string

def a_n_b_n():
    with open("a_n_b_n.txt", "r") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s = "aabb"
    assert s == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = "bbaa"
    assert "" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = "abbb"
    assert "ab" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = "abbbb"
    assert "ab" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = "bbab"
    assert "ab" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

def sci_not():
    with open("sci_not.txt", "r") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s = "+.e-0"
    assert s == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = "++e-0"
    assert "" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = "1+e-0"
    assert "" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = "1+e-"
    assert "" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

def brackets():
    with open("brackets.txt", "r") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s = "()"
    assert s == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = ")("
    assert "" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = "())"
    assert "()" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = "()()))"
    assert "()()" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = "()))()"
    assert "()()" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = "))))))"
    assert "" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

    s = "()()()("
    assert "()()()" == map_to_string(self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False, delete=True)[1], t_tab)

def main():
    a_n_b_n()
    sci_not()
    brackets()

if __name__ == "__main__":
    main()
