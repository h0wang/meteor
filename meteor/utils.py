import re
import typing

from .api import CurrencyPair, Side


def check_side(value: typing.Union[int, str, Side]) -> Side:
    if isinstance(value, str):
        value = value.lower()
        if value in ("bid", "buy", "bids", "b"):
            return Side.BID
        elif value in ("ask", "sell", "asks", "a"):
            return Side.ASK
    elif isinstance(value, int) and value == 1:
        return Side.BID
    elif isinstance(value, int) and value == -1:
        return Side.ASK
    elif isinstance(value, Side):
        return value
    raise ValueError(f"Unrecognised side `{value}`")


def check_currency_pair(*args, **kwargs) -> CurrencyPair:

    pattern = "(?P<base_ccy>[A-Za-z]{3,4}).*?(?P<quote_ccy>[A-Za-z]{3,4})"
    if "base_currency" in kwargs and "quote_currency" in kwargs:
        base_ccy = kwargs["base_currency"]
        quote_ccy = kwargs["quote_currency"]
        return CurrencyPair(base_currency=base_ccy, quote_currency=quote_ccy)

    if "product_id" in kwargs:
        product_id = kwargs["product_id"]
    elif "currency_pair" in kwargs:
        product_id = kwargs["currency_pair"]
    elif len(args) == 1:
        product_id, *_ = args
    elif len(args) >= 2 and len(args[0]) in [3, 4] and len(args[1]) in [3, 4]:
        base_ccy, quote_ccy, *_ = args
        return CurrencyPair(base_currency=base_ccy,
                            quote_currency=quote_ccy)
    else:
        raise ValueError("Cannot construct a `CurrencyPair` instance")

    if isinstance(product_id, CurrencyPair):
        return product_id

    m = re.match(pattern, product_id)
    if m:
        base_ccy = m.group("base_ccy")
        quote_ccy = m.group("quote_ccy")
        return CurrencyPair(base_currency=base_ccy, quote_currency=quote_ccy)
