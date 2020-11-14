from meteor.api import Currency, CurrencyPair


def test_bitcoin_cross():
    bitcoin_dollar_cross = CurrencyPair("XBT", "USD")
    assert bitcoin_dollar_cross.base_currency == Currency("xbt")
    assert bitcoin_dollar_cross.quote_currency == Currency("USD")

    bitcoin_sterling_cross = CurrencyPair("BTC", "gbp")
    assert bitcoin_sterling_cross.base_currency == Currency("btc")
    assert bitcoin_sterling_cross.quote_currency == Currency("GBP")


def test_bitcoin_cross_equal():
    btc_euro_cross = CurrencyPair("XBT", "EUR")
    xbt_euro_cross = CurrencyPair("BTC", "EUR")
    assert btc_euro_cross == xbt_euro_cross
