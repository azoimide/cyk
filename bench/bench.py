if __name__ == "__main__":
    
    nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar()
    # print data

    # print "nt_tab:", nt_tab
    # print "t_tab:", t_tab
    # print "nups:", nups
    # print "ups:", ups
    # print "rev_ups:", rev_ups


    # s = "()"
    # s = "(()())()"
    # s = map(lambda c: t_tab[c], s)
    # s = rand_string(t_tab, l=5)
    # print s
    # print cyk(nups, rev_ups, s, start, debug=True)
    # print derive(nups, ups, s, N=start)

    c = 100
    for l in range(1, 60):
        total = 0
        maxx = None
        for i in range(c):
            s = rand_string(t_tab, l)
            start_time = time()
            #derive(nups, ups, s, N=start, naive=True)
            #derive(nups, ups, s, N=start)
            cyk(nups, rev_ups, s, start)
            stop_time = time()
            total += stop_time - start_time
            if maxx == None or stop_time - start_time > maxx:
                maxx = stop_time - start_time
        print "{},{},{}".format(l, total / c, maxx)

