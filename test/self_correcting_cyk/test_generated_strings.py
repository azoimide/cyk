from cnf import read_grammar
from self_correcting_cyk import self_correcting_cyk
from util import map_string, map_to_string, levenshtein
from generate_string import generate_table, generate_string, rand_string

def main():
    with open("a_n_b_n.txt", "r") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

    for g in ["a_n_b_n.txt", "sci_not.txt", "brackets.txt"]:
        with open(g, "r") as f:
            nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

        for _ in range(100):
            s = rand_string(len(t_tab), 7)
            print s
            print map_to_string(s, t_tab)
            d, s2 = self_correcting_cyk(nups, ups, s, change=True, delete=True)
            print s2
            print map_to_string(s2, t_tab)
            l = levenshtein(s, s2)
            print "d:", d, "l:", l
            assert d == l
            print ""

if __name__ == "__main__":
    # main()
    print "WARNING: random tests don't work cuz levenshtein is symmetric"
