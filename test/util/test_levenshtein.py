from util import levenshtein

def main():
    assert 2 == levenshtein("abbbb", "aabb")
    assert 0 == levenshtein("aabb", "aabb")
    assert 1 == levenshtein("aaabb", "aabb")
    assert 1 == levenshtein("abbb", "aabb")

if __name__ == "__main__":
    main()
