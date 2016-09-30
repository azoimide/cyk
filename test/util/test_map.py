from util import map_string, map_to_string, rand_string

def main():
    t_tab = {'e': 5, '+': 2, '-': 3, '.': 4, '1': 1, '0': 0}
    s = rand_string(len(t_tab))
    assert s == map_string(map_to_string(s, t_tab), t_tab)

if __name__ == "__main__":
    main()
