import json

import pandas as pd

from ..api import Trade
from ..utils import check_currency_pair, check_side
from .base import Subscription
from .mixin import CoinbaseMixin, KrakenMixin


class CoinbaseTradeSubscription(Subscription, CoinbaseMixin):

    def __init__(self, *args, **kwargs):
        self.currency_pair = check_currency_pair(*args, **kwargs)

    @property
    def request(self):
        msg = {
            "type": "subscribe",
            "channels": [
                {
                    "name": "heartbeat",
                    "product_ids": [self.product_id]
                },
                {
                    "name": "full",
                    "product_ids": [self.product_id]
                }
            ]
        }
        return json.dumps(msg)

    @property
    def parser(self):
        def parse(msg):
            params = json.loads(msg)
            msg_type = params["type"]
            if msg_type == "match":
                currency_pair = check_currency_pair(**params)
                side = check_side(params["side"])
                timestamp = pd.to_datetime(params["time"])
                size = float(params["size"])
                price = float(params["price"])
                source = self.source
                trade = Trade(currency_pair=currency_pair, side=side,
                              price=price, size=size, timestamp=timestamp,
                              source=source)
                return (trade, )
            else:
                return None
        return parse


class KrakenTradeSubscription(Subscription, KrakenMixin):

    def __init__(self, *args, **kwargs):
        self.currency_pair = check_currency_pair(*args, **kwargs)

    @property
    def request(self):
        msg = {
            "event": "subscribe",
            "subscription": {
                    "name": "trade"
            },
            "pair": [f"{self.pair}"]
        }
        return json.dumps(msg)

    @property
    def parser(self):

        class _parser:

            def __init__(self, currency_pair):
                self.currency_pair = currency_pair

            def __call__(self, msg):
                params = json.loads(msg)
                if isinstance(params, list):
                    [_, trade_params, channel_name, _] = params
                    assert channel_name == "trade"
                    trades = []
                    for (price, size, timestamp, side, *_) in trade_params:
                        price = float(price)
                        size = float(size)
                        timestamp = pd.Timestamp(float(timestamp), unit="s")
                        side = check_side(side)
                        trade = Trade(currency_pair=self.currency_pair,
                                      side=side, price=price, size=size,
                                      timestamp=timestamp, source="kraken")
                        trades.append(trade)
                    return trades
                else:
                    return None

        return _parser(self.currency_pair)
