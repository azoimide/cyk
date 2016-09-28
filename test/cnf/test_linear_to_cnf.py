from cnf import read_linear_grammar
from cnf import linear_to_cnf

def main():
    fname = 'grammar_lin.txt'
    with open(fname, 'r') as f:
        lnups, rnups, ups, nt_tab, t_tab, start = read_linear_grammar(f)
    
    # print "lnups:", lnups
    # print "rnups:", rnups
    # print "ups:", ups
    # print "nt_tab:", nt_tab
    # print "t_tab:", t_tab
    # print ""

    nups, ups, nt_tab, t_tab = linear_to_cnf(lnups, rnups, ups, nt_tab, t_tab)

    # print "nups:", nups
    # print "ups:", ups
    # print "nt_tab:", nt_tab
    # print "t_tab:", t_tab

 
if __name__ == "__main__":
    main()
