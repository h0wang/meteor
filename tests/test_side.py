from meteor.api import Side


def test_bid():
    assert Side.BID.value == 1
    assert str(Side.BID) == "Bid"


def test_ask():
    assert Side.ASK.value == -1
    assert str(Side.ASK) == "Ask"


def test_bid_not_equal_to_ask():
    assert Side.BID != Side.ASK
