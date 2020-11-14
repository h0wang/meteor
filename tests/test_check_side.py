import pytest
from meteor.api import Side
from meteor.utils import check_side


def test_bid():
    assert check_side("bid") == Side.BID
    assert check_side("buy") == Side.BID
    assert check_side("bids") == Side.BID
    assert check_side(1) == Side.BID
    assert check_side("BID") == Side.BID
    assert check_side(Side.BID) == Side.BID


def test_ask():
    assert check_side("ask") == Side.ASK
    assert check_side("sell") == Side.ASK
    assert check_side("asks") == Side.ASK
    assert check_side(-1) == Side.ASK
    assert check_side("SELL") == Side.ASK
    assert check_side(Side.ASK) == Side.ASK


def test_with_invalid_value():
    with pytest.raises(ValueError):
        check_side("wrong value")


def test_with_none():
    with pytest.raises(ValueError):
        check_side(None)
