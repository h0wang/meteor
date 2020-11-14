import asyncio
import dataclasses
import datetime as dt
import enum
import typing


_CURRENCIES = {
    "USD": 1,
    "EUR": 2,
    "JPY": 3,
    "GBP": 4,

    "XAU": 11,
    "XAG": 12,

    "XBT": 101,
    "XET": 102,
    "BTC": 101,
    "ETH": 102,
    "USDT": 103,
    "USDC": 104
}


class Side(enum.Enum):
    BID = 1
    ASK = -1

    def __str__(self):
        if self == Side.BID:
            return "Bid"
        else:
            return "Ask"


@dataclasses.dataclass(init=True, repr=False, frozen=True, eq=False)
class Currency:
    value: str

    def __post_init__(self):
        object.__setattr__(self, "value", self.value.upper())

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if isinstance(other, Currency):
            id = _CURRENCIES[self.value]
            other_id = _CURRENCIES[other.value]
            return id == other_id
        return False


@dataclasses.dataclass(init=False, repr=False, frozen=True, eq=False)
class CurrencyPair:

    base_currency: Currency
    quote_currency: Currency

    def __init__(self, base_currency: typing.Union[str, Currency],
                 quote_currency: typing.Union[str, Currency]):
        if isinstance(base_currency, str):
            base_currency = Currency(base_currency)
        if isinstance(quote_currency, str):
            quote_currency = Currency(quote_currency)
        object.__setattr__(self, "base_currency", base_currency)
        object.__setattr__(self, "quote_currency", quote_currency)

    def __repr__(self):
        base_ccy = f"{self.base_currency!s}".upper()
        quote_ccy = f"{self.quote_currency!s}".upper()
        return f"{base_ccy}-{quote_ccy}"

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if isinstance(other, CurrencyPair):
            base_ccy = self.base_currency
            quote_ccy = self.quote_currency
            other_base_ccy = other.base_currency
            other_quote_ccy = other.quote_currency
            return base_ccy == other_base_ccy and \
                quote_ccy == other_quote_ccy
        return False


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
