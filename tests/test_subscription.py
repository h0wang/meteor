from meteor.subscription import CoinbaseTradeSubscription
from meteor.api import CurrencyPair


def test_trade_initialisation():
    coinbase_subscription = CoinbaseTradeSubscription(currency_pair="BTCUSD")
    desired_ccy_pair = CurrencyPair(base_currency="BTC", quote_currency="USD")
    assert coinbase_subscription.uri.startswith("wss://")
    assert coinbase_subscription.currency_pair == desired_ccy_pair
    assert callable(coinbase_subscription.parser)

    kraken_subscription = CoinbaseTradeSubscription(currency_pair="BTCUSD")
    desired_ccy_pair = CurrencyPair(base_currency="BTC", quote_currency="USD")
    assert kraken_subscription.uri.startswith("wss://")
    assert kraken_subscription.currency_pair == desired_ccy_pair
    assert callable(kraken_subscription.parser)
