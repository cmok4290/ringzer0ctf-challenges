# tests/test_hash_me_please.py
from coding_challenges import hash_me_please


def test_hash_me_please():
    flag = hash_me_please.main()
    assert isinstance(flag, str)
    assert flag.startswith('FLAG')
