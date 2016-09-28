from cnf import read_grammar
from self_correcting_cyk import self_correcting_cyk
from util import map_string

def main():
    with open("grammar.txt", "r") as f:
        nups, _, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    s1 = "bbcb"
    assert 0 == self_correcting_cyk(nups, rev_ups, map_string(s1, t_tab), debug=True)[0]

    s1 = "bbab"
    assert 1 == self_correcting_cyk(nups, rev_ups, map_string(s1, t_tab))[0]

if __name__ == "__main__":
    main()
