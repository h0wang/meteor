import json

import pandas as pd


from .base import Subscription
from .mixin import CoinbaseMixin

from ..utils import check_currency_pair, check_side
from ..api import Trade


class CoinbaseTradeSubscription(Subscription, CoinbaseMixin):

    def __init__(self, currency_pair):
        self.currency_pair = currency_pair

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
                return Trade(currency_pair=currency_pair, side=side,
                             price=price, size=size, timestamp=timestamp,
                             source=source)
            else:
                return None
        return parse
