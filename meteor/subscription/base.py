import abc


class Subscription:

    @property
    @abc.abstractmethod
    def request(self):
        pass

    @property
    @abc.abstractmethod
    def parser(self):
        pass
