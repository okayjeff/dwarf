"""
Temporary module. Controller functions will live in ~/elf.py and
routes will be built automatically based on decorators applied
to controller functions.
"""


def foo_func(request):
    return 'HTTP/1.1 200 OK\n\nI am FOO!'


def bar_func(request):
    return 'HTTP/1.1 200 OK\n\nI am BAR!'

routes = {
    '^/foo/?$': foo_func,
    '^/bar/?$': bar_func,
}
