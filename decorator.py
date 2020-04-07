def decorator_function(original_fun):
    def wrapper():
        return original_fun()
    return wrapper

def display():
    print("Display something.")

decorated_fun = decorator_function(display)
decorated_fun()

@decorator_function
def display2():
    print("Display something.")


display2()



def decorator_function(original_fun):
    def wrapper():
        return original_fun()
    return wrapper


@decorator_function
def display():
    print("Display something.")


display()


