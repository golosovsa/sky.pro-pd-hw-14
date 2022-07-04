"""
    GRM package
    Patterns meta classes
"""


class Singleton(type):
    """ Singleton metaclass. There can only be a unique instance. """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        cls._instance.__init__(*args, **kwargs)
        return cls._instance
