# tests/test_coding_challenges.py
from coding_challenges import hash_me_reloaded


def test_hash_me_releaded():
    flag = hash_me_reloaded.main()
    assert isinstance(flag, str)
    assert flag.startswith('FLAG')
