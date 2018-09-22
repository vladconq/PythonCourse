import sys
from contextlib import redirect_stderr
from contextlib import redirect_stdout


def stderr_redirect(dest=None):
    def real_decorator(func):
        def wrapper():
            with open(dest, 'a+') as f:
                with redirect_stderr(f):
                    return func()

        return wrapper

    return real_decorator


@stderr_redirect(dest='file1')
def test1():
    sys.stderr.write('test1 func\n')
    return 10


@stderr_redirect(dest='file2')
def test2():
    test1()
    sys.stderr.write('test2 func\n')

    return 10 + test1()


print(test2())
