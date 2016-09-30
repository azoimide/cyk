import random

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

def levenshtein(s1, s2, i1=None, i2=None):
    if i1 == None:
        i1 = len(s1)
    if i2 == None:
        i2 = len(s2)


    if i1 == 0:
        return i2
    if i2 == 0:
        return i1

    if s1[i1 - 1] == s2[i2 - 1]:
        cost = 0
    else:
        cost = 1

    return min(levenshtein(s1, s2, i1 - 1, i2) + 1,
               levenshtein(s1, s2, i1, i2 - 1) + 1,
               levenshtein(s1, s2, i1 - 1, i2 - 1) + cost)

def rand_string(t_count, l=10):
    r = random.Random()
    return [ r.randint(0, t_count - 1) for i in range(l) ]
