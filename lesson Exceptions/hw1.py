def stderr_redirect(dest=None):
    def real_decorator(func):
        def wrapper():
            if dest == None:
                result = func()
                print(result)
            else:
                with open(dest, 'w') as fd:
                    try:
                        result = func()
                    except Exception as error:
                        print(error, file=fd)
                    else:
                        print(result, file=fd)

        return wrapper

    return real_decorator


@stderr_redirect(dest='output')
def func_with_error():
    return ("1234" + 1)


func_with_error()
