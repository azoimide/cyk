import sys
from cnf import read_grammar

if __name__ == "__main__":
    fname = 'grammar_lin.txt'
    with open(fname, 'r') as f:
        nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)
    # print "nups:", nups
    # print "ups:", ups
    # print "rev_ups:", rev_ups
    # print "nts:", nt_tab
    # print "ts:", t_tab
    # print "start:", start
