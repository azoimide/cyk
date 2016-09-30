from cnf import read_grammar
from self_correcting_cyk import self_correcting_cyk, self_correcting_cyk2, self_correcting_cyk3, self_correcting_cyk4
from util import map_string

def main():
    with open("grammar.txt", "r") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    print sorted(nt_tab, key=lambda k: nt_tab[k])

    # Only changes
    s = "aabb"
    assert 0 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[0]

    s = "bbaa"
    assert 4 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[0]

    s = "abbb"
    assert 1 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[0]

    s = "abbbb"
    assert len(s) < self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[0]

    s = "bbab"
    assert 3 == self_correcting_cyk(nups, ups, map_string(s, t_tab), debug=False)[0]

    # Only deletions
    s = "abb"
    assert 1 == self_correcting_cyk2(nups, ups, map_string(s, t_tab), debug=False)[0]

    s = "aab"
    assert 1 == self_correcting_cyk2(nups, ups, map_string(s, t_tab), debug=False)[0]

    s = "abbbb"
    assert 3 == self_correcting_cyk2(nups, ups, map_string(s, t_tab), debug=False)[0]

    s = "aabbb"
    assert 1 == self_correcting_cyk2(nups, ups, map_string(s, t_tab), debug=False)[0]

    s = "abaab"
    assert 3 == self_correcting_cyk2(nups, ups, map_string(s, t_tab), debug=False)[0]

    # Deletions and changes
    s = "abbbb"
    assert 2 == self_correcting_cyk3(nups, ups, map_string(s, t_tab), debug=False)[0]

    s = "aabbb"
    assert 1 == self_correcting_cyk3(nups, ups, map_string(s, t_tab), debug=False)[0]

    s = "bbb"
    assert 2 == self_correcting_cyk3(nups, ups, map_string(s, t_tab), debug=False)[0]

    s = "abaab"
    assert 2 == self_correcting_cyk3(nups, ups, map_string(s, t_tab), debug=False)[0]

    # Find closest string
    s = "abbbb"
    assert 2 == self_correcting_cyk4(nups, ups, map_string(s, t_tab), debug=True)[0]
    
    s = "bbaab"
    assert 3 == self_correcting_cyk4(nups, ups, map_string(s, t_tab), debug=True)[0]

if __name__ == "__main__":
    main()
