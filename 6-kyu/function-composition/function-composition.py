def compose(f, g):
    """
    Compose two functions f and g.
    Returns a new function that applies g first, then f.

    compose(f, g)(x) is equivalent to f(g(x))
    """

    def composed_function(*args, **kwargs):
        # Apply g to the arguments, then apply f to the result
        return f(g(*args, **kwargs))

    return composed_function
