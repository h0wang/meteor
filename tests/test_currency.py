from meteor.api import Currency


def test_bitcoin():
    xbt = Currency("XBT")
    assert xbt.value == "XBT"
    assert f"{xbt!s}" == "XBT"
    assert f"{xbt!r}" == "XBT"


def test_sterling():
    gbp = Currency("gbp")
    assert f"{gbp!s}" == "GBP"
    assert f"{gbp!r}" == "GBP"


def test_tether():
    tether = Currency("USDT")
    assert f"{tether!s}" == "USDT"
    assert f"{tether!s}" == "USDT"


def test_btc_xbt_equal():
    xbt = Currency("XBT")
    btc = Currency("btc")
    assert xbt == btc


def test_etc_xet_equal():
    xet = Currency("xet")
    etc = Currency("ETh")
    assert xet == etc
