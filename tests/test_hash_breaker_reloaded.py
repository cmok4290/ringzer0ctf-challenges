# tests/test_hash_breaker_reloaded.py
from coding_challenges import hash_breaker_reloaded


def test_hash_breaker_reloaded():
    flag = hash_breaker_reloaded.main()
    assert isinstance(flag, str)
    assert flag.startswith('FLAG')
