def do_twice(function, function_args):
    function(function_args)
    function(function_args)


def print_spam():
    print('spam')


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(function, function_args):
    do_twice(function, function_args)
    do_twice(function, function_args)


if __name__ == "__main__":
    do_twice(print_twice, 'spam')
    do_four(print_twice, '>>>> spam')
