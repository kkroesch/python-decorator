class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Registry(metaclass=Singleton):
    """Management for plugins as a singleton.
    """
    
    def __init__(self):
        self._plugins = dict()
    
    def register(self, func):
        self._plugins[func.__name__] = func
        return func

    def get_plugins(self):
        return self._plugins.items()

    def doc_plugins(self):
        return [(name, func.__doc__) for name, func in self._plugins.items()]


def register(func):
    Registry().register(func)
