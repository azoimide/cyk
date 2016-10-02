# from cnf import read_grammar
# from self_correcting_cyk import self_correcting_cyk, self_correcting_cyk2, self_correcting_cyk3, self_correcting_cyk4
# from util import map_string, map_to_string, levenshtein
# from generate_string import generate_table, generate_string, rand_string

# def main():
#     with open("a_n_b_n.txt", "r") as f:
#         nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

#     # Find closest string
#     s = map_string("abbbb", t_tab)
#     d, s2 = self_correcting_cyk4(nups, ups, s, debug=False)
#     assert d == levenshtein(s, s2)

#     s = map_string("abaab", t_tab)
#     d, s2 = self_correcting_cyk4(nups, ups, s, debug=False)
#     assert d == levenshtein(s, s2)
    
#     # s = "bbaab"
#     # assert 3 == self_correcting_cyk4(nups, ups, map_string(s, t_tab), debug=True)[0]
    
#     with open("a_n_b_n.txt", "r") as f:
#     # with open("sci_not.txt", "r") as f:
#         nups, ups, rev_ups, nt_tab, t_tab, start = read_grammar(f)

#     print t_tab

#     # for l in range(5, 7):
#     #     tab = generate_table(nups, ups, start, l)
#     #     for _ in range(5):
#     #         s = generate_string(nups, ups, tab)
#     #         print s
#     #         print map_to_string(s, t_tab)
#     #         d, s2 = self_correcting_cyk4(nups, ups, s, debug=False)
#     #         print s2
#     #         print map_to_string(s2, t_tab)
#     #         print d
#     #         assert d == levenshtein(s, s2)

#     for _ in range(100):
#         s = rand_string(len(t_tab), 7)
#         print s
#         print map_to_string(s, t_tab)
#         d, s2 = self_correcting_cyk4(nups, ups, s, debug=False)
#         print s2
#         print map_to_string(s2, t_tab)
#         l = levenshtein(s, s2)
#         print "d:", d, "l:", l
#         assert d == l

# if __name__ == "__main__":
#     main()
