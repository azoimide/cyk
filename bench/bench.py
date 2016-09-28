from time import time

from cyk.cnf import read_grammar, read_linear_grammar
from cyk.cyk import cyk_td, cyk_bu, linear_cyk
from cyk.generate_string import rand_string

if __name__ == "__main__":
    
    nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar()

    c = 100
    for l in range(1, 60):
        total = 0
        for i in range(c):
            s = rand_string(len(t_tab), l)
            start_time = time()
            # cyk_td(nups, ups, s, N=start, naive=True)
            cyk_td(nups, ups, s, N=start)
            # cyk_bu(nups, rev_ups, s, start)
            stop_time = time()
            total += stop_time - start_time
        print "{},{}".format(l, total / c)

