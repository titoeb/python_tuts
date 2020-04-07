import requests

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero!')
    else:
        return x / y

def get_website():
    response = requests.get(f"http://company.com/tim/1")
    if response.ok:
        return response.text
    else:
        return 'Bad Response!'