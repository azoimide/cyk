def print_arr(a):
    print "\n".join(map(str, a))
    print ""

def map_string(s, t_tab):
    return map(lambda c: t_tab[c], s)

def map_to_string(ns, t_tab):
    s = ""
    for n in ns:
        for c in t_tab.keys():
            if t_tab[c] == n:
                s += c
                break
    return s
