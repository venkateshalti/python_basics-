import main_function  # this will print corresponding mandatory message
from simplepackage import main_function as main_func
print('hello')
print(main_function.__name__)  # value is set to its own module name instead of '__main__'
print(main_func.__name__)  # value is set to its own module name(with package name) instead of '__main__'