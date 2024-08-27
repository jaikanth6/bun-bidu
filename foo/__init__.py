from .core import Foo

class BarProxy:
    def __init__(self, parent):
        self._parent = parent

    def __getattr__(self, name):
        original_attr = getattr(self._parent, name)
        if callable(original_attr):
            def wrapper(*args, **kwargs):
                print(f"Pre-processing for {name}")
                result = original_attr(*args, **kwargs)
                print(f"Post-processing for {name}")
                return result
            return wrapper
        return original_attr

class FooWithBar(Foo):
    def __init__(self):
        super().__init__()
        self.bar = BarProxy(self)

# Create an instance and replace the module with it
import sys
sys.modules[__name__] = FooWithBar()