def example_function(arg1, *args, kwarg1="default", **kwargs):
    print("arg1:", arg1)
    print("args:", args)
    print("kwarg1:", kwarg1)
    print("kwargs:", kwargs)


example_function(1, 2, 3, kwarg1="custom", name="John", age=30)
