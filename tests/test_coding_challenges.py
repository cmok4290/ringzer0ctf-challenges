# tests/test_coding_challenges.py

from coding_challenges import (
    hash_me_please,
    hash_me_reloaded,
    i_hate_mathematics,
    hash_breaker,
    hash_breaker_reloaded
)


class TestCodingChallenges:
    def test_hash_me_please(self):
        flag = hash_me_please.main()
        assert isinstance(flag, str)
        assert flag.startswith('FLAG')

    def test_hash_me_releaded(self):
        flag = hash_me_reloaded.main()
        assert isinstance(flag, str)
        assert flag.startswith('FLAG')

    def test_i_hate_mathematics(self):
        flag = i_hate_mathematics.main()
        assert isinstance(flag, str)
        assert flag.startswith('FLAG')

    def test_hash_breaker(self):
        flag = hash_breaker.main()
        assert isinstance(flag, str)
        assert flag.startswith('FLAG')

    def test_hash_breaker_reloaded(self):
        flag = hash_breaker_reloaded.main()
        assert isinstance(flag, str)
        assert flag.startswith('FLAG')
