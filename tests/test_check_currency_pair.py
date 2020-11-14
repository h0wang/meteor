import pytest
from meteor.api import CurrencyPair
from meteor.utils import check_currency_pair


def test_six_chars_pair():

    xbt_usd = check_currency_pair("XBTUSD")
    assert xbt_usd == CurrencyPair(base_currency="XBT", quote_currency="USD")


def test_pair_with_slash():

    btc_usd = check_currency_pair("BTC/USD")
    assert btc_usd == CurrencyPair(base_currency="BTC", quote_currency="USD")


def test_pair_with_dash():

    etc_usd = check_currency_pair("ETH-USD")
    assert etc_usd == CurrencyPair(base_currency="ETH", quote_currency="USD")


def test_more_than_six_chars_pair():

    btc_usdt = check_currency_pair("BTC/USDT")
    assert btc_usdt == CurrencyPair(base_currency="BTC", quote_currency="USDT")


def test_with_named_params():
    gbp_usd = check_currency_pair(base_currency="gbp", quote_currency="usd",
                                  ignored="should not be used")
    assert gbp_usd == CurrencyPair(base_currency="GBP", quote_currency="USD")

    usd_yen = check_currency_pair(product_id="usd/jpy")
    assert usd_yen == CurrencyPair(base_currency="USD", quote_currency="JPY")


def test_pair_instance():
    eur_yen = check_currency_pair(CurrencyPair("EUR", "JPY"))
    assert eur_yen == CurrencyPair(base_currency="EUR", quote_currency="JPY")


def test_with_positioning_params():
    eth_usdt = check_currency_pair("eth", "usdt", "ignored", 12, None)
    assert eth_usdt == CurrencyPair(base_currency="ETH", quote_currency="USDT")


def test_with_no_params():
    with pytest.raises(ValueError):
        check_currency_pair()
