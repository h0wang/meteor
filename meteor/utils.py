import re
import typing

from .api import CurrencyPair, Side


def check_side(value):
    if value.lower() in ("bid", "buy", "bids"):
        return Side.BID
    elif value.lower() in ("ask", "sell", "asks"):
        return Side.ASK
    else:
        raise ValueError(f"Unrecognised side `{value}`")


def check_currency_pair(*args, **kwargs):

    pattern = "(?P<base_currency>[A-Z]{3}).*?(?P<quote_currency>[A-Z]{3})"
    if "base_currency" in kwargs and "quote_currency" in kwargs:
        base_currency = kwargs["base_currency"]
        quote_currency = kwargs["quote_currency"]
        return CurrencyPair(base_currency=base_currency,
                            quote_currency=quote_currency)

    if "product_id" in kwargs:
        product_id = kwargs["product_id"]
    elif len(args) == 1:
        product_id, *_ = args

    if isinstance(product_id, CurrencyPair):
        return product_id

    m = re.match(pattern, product_id)
    if m:
        base_currency = m.group("base_currency")
        quote_currency = m.group("quote_currency")
        return CurrencyPair(base_currency=base_currency,
                            quote_currency=quote_currency)

    if len(args) == 2 and len(args[0]) == 3 and len(args[1]) == 3:
        base_currency = args[0]
        quote_currency = args[1]
        return CurrencyPair(base_currency=base_currency,
                            quote_currency=quote_currency)

    raise ValueError("Cannot construct a `CurrencyPair` instance")
