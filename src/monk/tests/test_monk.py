import pytest
from monk import Monk

def test_equal():
  assert Monk.safe_eval("1.1 == 1.1") is True

def test_not_equal():
  assert Monk.safe_eval("1 == 2") is False

def test_greater_than():
  assert Monk.safe_eval("1 > 2") is False

def test_less_than():
  assert Monk.safe_eval("1 < 2") is True

def test_greater_equal():
  assert Monk.safe_eval("1 >= 2") is False

def test_less_equal():
  assert Monk.safe_eval("1 <= 2") is True

def test_chained_comparison_true():
  assert Monk.safe_eval("1 < 2 < 3 < 4") is True

def test_chained_comparison_false():
  assert Monk.safe_eval("1 < 2 < 3 > 4") is False

def test_string_comparison():
  assert Monk.safe_eval("'cat' == 4") is False

def test_invalid_syntax():
  with pytest.raises(SyntaxError):
    Monk.safe_eval("1 + 2")
  
def test_lots():
    assert Monk.safe_eval("1.1 == 1.1") is True
    assert Monk.safe_eval("1 == 2") is False
    assert Monk.safe_eval("1 > 2") is False
    assert Monk.safe_eval("1 < 2") is True
    assert Monk.safe_eval("1 >= 2") is False
    assert Monk.safe_eval("1 <= 2") is True
    assert Monk.safe_eval("1 < 2 < 3 < 4") is True
    assert Monk.safe_eval("1 < 2 < 3 > 4") is False
    assert Monk.safe_eval("'cat' == 4") is False
