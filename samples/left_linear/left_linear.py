from cyk.cnf import read_grammar
from cyk.generate_string import generate_string
from cyk.util import map_to_string

if __name__ == "__main__":
    with open("left_linear.txt") as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)
    s = generate_string(nups, ups, length=10)
    print map_to_string(s, t_tab)

