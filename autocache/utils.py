import collections


def convert_to_tuple(el):
    """Converts recursively list/dict into hashable tuples."""
    if isinstance(el, (tuple, list)):
        # Convert recursively tuple content
        return tuple(convert_to_tuple(e) for e in el)
    if isinstance(el, dict):
        return tuple((label, convert_to_tuple(value))
                     for label, value in sorted(el.items(), key=lambda item: item[0]))
    if isinstance(el, collections.Hashable):
        return el
    raise TypeError('%r is not hashable.' % el)
