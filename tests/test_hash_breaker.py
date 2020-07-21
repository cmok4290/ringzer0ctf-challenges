# tests/test_hash_breaker.py
from coding_challenges import hash_breaker


def test_hash_breaker():
    flag = hash_breaker.main()
    assert isinstance(flag, str)
    assert flag.startswith('FLAG')
