from copy import deepcopy


def partial(func, *fixated_args, **fixated_kwargs):
    def inner(*args, **kwargs):
        new_args = fixated_args + args
        new_kwargs = deepcopy(fixated_kwargs)
        new_kwargs.update(kwargs)
        return func(*new_args, **new_kwargs)

    args_doc = ' '.join(fixated_args)
    kwargs_doc = ' '.join(['%s=%s' % (k, v) for k, v in fixated_kwargs.items()])
    name = func.__name__
    doc = 'A partial implementation of %s\nwith pre-apllied arguments being:\n%s %s'
    inner.__doc__ = doc % (name, args_doc, kwargs_doc)
    inner.__name__ = 'partial_%s' % name
    return inner


pp = partial(print, 'Hello', end='!')
print(pp.__name__)
print(pp.__doc__)
pp('world', sep=', ')
