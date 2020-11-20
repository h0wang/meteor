meteor
======

``meteor`` is a library for collecting market data from popular cryptocurrency exchanges via web socket using Python 3.8 or above.

Basic Useage
------------

.. code-block:: python

    import asyncio

    from meteor import Subscriber
    from meteor.subscription import CoinbaseTradeSubscription

    event_loop = asyncio.get_event_loop()
    queue = asyncio.Queue()

    subscription = CoinbaseTradeSubscription("BTCUSD")
    subscriber = Subscriber(subscription, queue)

    event_loop.run_until_complete(subscriber.subscribe())

Demonstration
-------------

    $ python -m meteor --currency_pair BTCUSD ETHGBP

License
-------

meteor is developed and distributed under the Apache 2.0 license.
