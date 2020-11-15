from ..utils import check_currency_pair


class CoinbaseMixin:

    @property
    def source(self):
        return "coinbase pro"

    @property
    def product_id(self):
        pair = getattr(self, "currency_pair")
        pair = check_currency_pair(pair)
        base_ccy = pair.base_currency
        quote_ccy = pair.quote_currency
        return f"{base_ccy}-{quote_ccy}"

    @property
    def uri(self):
        return "wss://ws-feed.pro.coinbase.com"


class KrakenMixin:

    @property
    def source(self):
        return "kraken"

    @property
    def pair(self):
        pair = getattr(self, "currency_pair")
        pair = check_currency_pair(pair)
        base_ccy = pair.base_currency
        quote_ccy = pair.quote_currency
        return f"{base_ccy}/{quote_ccy}"

    @property
    def uri(self):
        return "wss://ws.kraken.com/"
