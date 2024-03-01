
class DictBase(dict):
    """dict like object that exposes keys as attributes"""

    __slots__ = ()
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


    def update(self, *args, **kwargs):
        """update and return self -- the missing dict feature in python"""
        super().update(*args, **kwargs)
        return self
