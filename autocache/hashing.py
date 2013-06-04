import hashlib
import inspect

from autocache.utils import convert_to_hashable


def md5(value):
    """
    Helper function that returns an MD5 hash of the passed value, allowing a
    more pluggable hash implementation than requiring all hash functions to
    support the `hashlib` API.
    """
    return hashlib.md5(value).hexdigest()


# Callable Hashing

def bytecode_hash(function, hash=md5):
    """
    Returns the hashed bytecode for the provided callable.
    """
    return hash(function.func_code.co_code)


def source_hash(function, hash=md5):
    """
    Returns the hashed source for the provided callable.
    """
    return hash(inspect.getsource(function))


# Argument Hashing

def argument_hash(function, *args, **kwargs):
    # TODO: Allow usage of a different postprocessor than MD5.
    # TODO: Replace `hash` with a safe hashing implementation.

    arguments = inspect.getcallargs(function, *args, **kwargs)
    arguments = convert_to_hashable(arguments)
    return md5(':'.join(map(lambda value: str(hash(value)), arguments)))
