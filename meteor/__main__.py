import argparse
import asyncio

from meteor import ConsolePublisher, Subscriber
from meteor.subscription import BitstampTradeSubscription as BSTP
from meteor.subscription import CoinbaseTradeSubscription as COIN
from meteor.subscription import KrakenTradeSubscription as KRKN

APP_NAME = "asyn-meteor"
APP_DESCRIPTION = "Asynchronised Crypto Market Data Collection Module"


def main(currency_pairs):

    event_loop = asyncio.get_event_loop()
    queue = asyncio.Queue()

    for pair in currency_pairs:
        for s in [COIN(pair), BSTP(pair), KRKN(pair)]:
            subscriber = Subscriber(subscription=s, queue=queue)
            event_loop.create_task(subscriber.subscribe())

    publisher = ConsolePublisher(queue)
    publisher_task = event_loop.create_task(publisher.publish())
    event_loop.run_until_complete(publisher_task)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog=APP_NAME,
                                     description=APP_DESCRIPTION)
    parser.add_argument("-c", "--currency_pair", type=str, nargs="+",
                        dest="currency_pair",
                        help="currency pairs to collect")
    args = parser.parse_args()

    currency_pairs = [c.upper() for c in args.currency_pair]

    main(currency_pairs)
