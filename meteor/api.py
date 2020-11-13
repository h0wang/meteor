import asyncio
import dataclasses
import datetime as dt
import enum
import typing


class Side(enum.Enum):
    BID = 1
    ASK = -1

    def __str__(self):
        if self == Side.BID:
            return "Bid"
        else:
            return "Ask"


@dataclasses.dataclass(init=True, repr=False, frozen=True)
class CurrencyPair:

    base_currency: str
    quote_currency: str

    def __repr__(self):
        return f"{self.base_currency}-{self.quote_currency}"

    @classmethod
    def from_descriptor(cls, **kwargs):
        print(kwargs)
        if "product_id" in kwargs:
            product_id = kwargs["product_id"]
            base_currency = product_id[:3]
            quote_currency = product_id[-3:]
            return CurrencyPair(base_currency=base_currency,
                                quote_currency=quote_currency)


@dataclasses.dataclass
class Trade:

    currency_pair: CurrencyPair
    side: Side
    price: float
    size: float
    timestamp: dt.datetime
    source: str


@dataclasses.dataclass
class Quote:

    currency_pair: CurrencyPair
    side: Side
    price: float
    size: float
    timestamp: dt.datetime
    source: str


@dataclasses.dataclass
class Orderbook:

    currency_pair: CurrencyPair
    bids: typing.List[Quote]
    asks: typing.List[Quote]
    timestamp: dt.datetime

    @property
    def best_bid(self) -> float:
        return self.bids[0].price

    @property
    def best_ask(self) -> float:
        return self.asks[0].price

    @property
    def mid(self) -> float:
        return (self.best_bid + self.best_ask) / 2

    @property
    def spread(self) -> float:
        return self.best_ask - self.best_bid
