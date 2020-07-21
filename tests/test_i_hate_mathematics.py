# tests/test_i_hate_mathematics.py
from coding_challenges import i_hate_mathematics


def test_i_hate_mathematics():
    flag = i_hate_mathematics.main()
    assert isinstance(flag, str)
    assert flag.startswith('FLAG')
