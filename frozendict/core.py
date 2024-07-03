from .stringconstant import StringConstant as sc

class frozendictbase(dict):
    """
    This class is identical to frozendict, but without the slots. Useful for
    inheriting.
    """

    @classmethod
    def fromkeys(cls, seq, value=None, *args, **kwargs):
        return cls(dict.fromkeys(seq, value, *args, **kwargs))

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self._initialized = False
        return self

    def __init__(self, *args, **kwargs):
        """
        Identical to dict.__init__(). It can't be reinvoked
        """
        
        classname = type(self).__name__

        self._immutable_err = sc.immutable_tpl.format(klass=classname)

        if self._initialized:
            raise NotImplementedError(self._immutable_err)

        super().__init__(*args, **kwargs)

        # check if all values are immutable, like frozenset
        for v in self.values():
            hash(v)
        
        self._hash = hash(frozenset(self.items()))

        self._repr = sc.class_repr_tpl.format(
            klass = classname, 
            body = super().__repr__()
        )

        self._initialized = True
    
    def __hash__(self):
        return self._hash
    
    def __repr__(self):
        return self._repr
    
    def __add__(self, other):
        """
        If you add a dict-like object, a new frozendict will be returned, equal 
        to the old frozendict updated with the other object.
        """

        tmp = dict(self)

        try:
            tmp.update(other)
        except Exception:
            raise TypeError(sc.add_err_tpl.format(
                klass1 = type(self).__name__, 
                klass2 = type(other).__name__
            ))
        
        return self.__class__(tmp)

    def __sub__(self, iterable):
        """
        You can subtract an iterable from a frozendict. A new frozendict
        will be returned, without the keys that are in the iterable.
        """

        try:
            iter(iterable)

            if isinstance(iterable, (str, bytes, bytearray)):
                raise TypeError()
        except Exception:
            raise TypeError(sc.sub_err_tpl.format(
                klass1 = type(self).__name__, 
                klass2 = type(iterable).__name__
            ))

        return self.__class__({k: v for k, v in self.items() if k not in iterable})

    def __reduce__(self):
        return (self.__class__, (dict(self), ))


    def __setattr__(self, *args, **kwargs):
        """
        not implemented
        """
        
        try:
            initialized = self._initialized
        except Exception:
            initialized = False

        if initialized:
            raise NotImplementedError(self._immutable_err)

        super().__setattr__(*args, **kwargs)

    def __delattr__(self, *args, **kwargs):
        """
        not implemented
        """

        raise NotImplementedError(self._immutable_err)

    def __delitem__(self, *args, **kwargs):
        """
        not implemented
        """
        
        raise NotImplementedError(self._immutable_err)

    def __setitem__(self, *args, **kwargs):
        """
        not implemented
        """
        
        raise NotImplementedError(self._immutable_err)

    def clear(self, *args, **kwargs):
        """
        not implemented
        """
        
        raise NotImplementedError(self._immutable_err)

    def pop(self, *args, **kwargs):
        """
        not implemented
        """
        
        raise NotImplementedError(self._immutable_err)

    def popitem(self, *args, **kwargs):
        """
        not implemented
        """
        
        raise NotImplementedError(self._immutable_err)

    def setdefault(self, *args, **kwargs):
        """
        not implemented
        """
        
        raise NotImplementedError(self._immutable_err)

    def update(self, *args, **kwargs):
        """
        not implemented
        """
        
        raise NotImplementedError(self._immutable_err)

class frozendict(frozendictbase):
    """
    A simple immutable dictionary.

    The API is the same as `dict`, without methods that can change the 
    immutability.
    In addition, it supports the __add__ and __sub__ operands.
    """

    __slots__ = ("_initialized", "_hash", "_repr", "_immutable_err")


__all__ = (frozendict.__name__, frozendictbase.__name__)
