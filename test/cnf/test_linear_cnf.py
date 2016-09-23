import sys
from cnf import read_linear_grammar

if __name__ == "__main__":
    fname = 'grammar_lin.txt'
    with open(fname, 'r') as f:
        lnups, rnups, ups, nt_tab, t_tab, start = read_linear_grammar(f)
    # print "rnups:", rnups
    # print "lnups:", lnups
    # print "ups:", ups
    # print "nts:", nt_tab
    # print "ts:", t_tab
    # print "start:", start
