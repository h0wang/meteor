from .impl import (BitstampTradeSubscription, CoinbaseTradeSubscription,
                   KrakenTradeSubscription)

BSTP = BitstampTradeSubscription
COIN = CoinbaseTradeSubscription
KRKN = KrakenTradeSubscription


__all__ = ["BitstampTradeSubscription",
           "CoinbaseTradeSubscription",
           "KrakenTradeSubscription",
           "BSTP", "COIN", "KRKN"]
