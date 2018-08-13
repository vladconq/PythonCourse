def make_cache(number_of_calls):
    def decorator(fun):
        set_of_names = set()

        def wrapper(name):
            nonlocal set_of_names
            if len(set_of_names) == number_of_calls:
                print("I again forgot everything.")
                set_of_names = set()
            if name not in set_of_names:
                print("I can only remember three names.")
                set_of_names.add(name)
                print("Now they are: " + str(set_of_names) + '\n')
            else:
                print("I already remembered " + name + "!" + '\n')

        return wrapper

    return decorator


@make_cache(3)
def slow_function(name):
    return name


slow_function("Ivan")
slow_function("Sveta")
slow_function("Sveta")
slow_function("Misha")
slow_function("Tanya")
slow_function("Stepa")
