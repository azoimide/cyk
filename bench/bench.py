import sys
from time import time

from cyk.cnf import read_grammar, read_linear_grammar
from cyk.cyk import cyk_td, cyk_bu, linear_cyk
from cyk.generate_string import rand_string, generate_table, generate_string

def use_and_exit():
    print "Use: {} {{td|bu|naive}} {{rand|gen}}".format(sys.argv[0])
    sys.exit(1)

if __name__ == "__main__":
    algs = ["td", "bu", "naive"]
    modes = ["rand", "gen"]
    if len(sys.argv) != 3 or sys.argv[1] not in algs or sys.argv[2] not in modes:
        use_and_exit()
    alg = sys.argv[1]
    mode = sys.argv[2]

    
    nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar()

    c = 100
    for l in range(1, 60):
        total = 0
        if mode == "gen":
            gen_tab = generate_table(nups, ups, start, l)
            if not gen_tab[start][-1]:
                continue

        for i in range(c):
            if mode == "gen":
                s = generate_string(nups, ups, gen_tab)
            elif mode == "rand":
                s = rand_string(len(t_tab), l)

            start_time = time()

            if alg == "td":
                cyk_td(nups, ups, s, N=start)
            elif alg == "bu":
                cyk_bu(nups, rev_ups, s, start)
            elif alg == "naive":
                cyk_td(nups, ups, s, N=start, naive=True)

            stop_time = time()
            total += stop_time - start_time
        print "{},{}".format(l, total / c)
        if total > 5:
            break

