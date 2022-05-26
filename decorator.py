def merge_sort_decorator(func):
    open('dataset_execution_times', 'wb').close()

    def wrapper(arg):
        res = func(arg)
        return res
    return wrapper
