from util import levenshtein

def main():
    test_symmetric()
    print "WARNING: skipped asymmetric levenshtein!"
    # test_asymmetric()

def test_symmetric():
    assert 2 == levenshtein("abbbb", "aabb")
    assert 0 == levenshtein("aabb", "aabb")
    assert 1 == levenshtein("aaabb", "aabb")
    assert 1 == levenshtein("abbb", "aabb")

def test_asymmetric():
    l = levenshtein(".e0-010", "+.e-010", sym=False)
    print l
    assert 3 == l

    l = levenshtein("bbaabab", "aabb", sym=False)
    print l
    assert 3 == l

    l = levenshtein("e1e-ee0", "+1.e+0", sym=False)
    print l
    assert 4 == l

    l = levenshtein("+++e+-1", "+.e-1", sym=False)
    print l
    assert 3 == l

    l = levenshtein("))(())(", "()(())", sym=False)
    print l
    assert 2 == l

    l = levenshtein(".e-010.", "+.e+100", sym=False)
    print l
    assert 5 == l

    l = levenshtein("", "", sym=False)
    print l
    assert 0 == l

if __name__ == "__main__":
    main()

