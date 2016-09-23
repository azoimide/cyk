from cnf import read_grammar
from generate_string import generate_table, generate_string

if __name__ == "__main__":
    fname = 'grammar_cnf.txt'
    with open(fname, 'r') as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)
    # print "nups:", nups
    # print "ups:", ups
    # print "rev_ups:", rev_ups
    # print "nts:", nt_tab
    # print "ts:", t_tab
    # print "start:", start

    tab = generate_table(nups, ups, 0, 12, debug=False)
    # print "tab:"


    s = generate_string(nups, ups, tab, debug=False)
    # print "s:", s


