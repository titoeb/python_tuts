def decorator_function(fun):
    def wrapper(*args, **kwargs):
        return fun(*args, **kwargs)
    return wrapper

@decorator_function
def test_fun_with_args(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

test_fun_with_args('argument 1', 'argument 2')