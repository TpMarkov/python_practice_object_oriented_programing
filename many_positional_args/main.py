def add(*args):  # *args when you know there will be a number of args passed in to the function ,but you don't know exactly how many.
    print(type(args))  # tuple
    print(args)  # (1,2,3)


add(1, 2, 3)


def function_with_named_arguments(n, **dict_args):
    print(dict_args)  # {arg_1:1,arg_2=2}
    print(type(dict_args))

    # iterate libs
    for key, value in dict_args.items():
        print(f"{key}: {value}")

    print(n + dict_args["arg_1"])


function_with_named_arguments(2, arg_1=1,
                              arg_2=2)  # Need to declare the arguments like this when calling a function with **args


# Optional arguments in Class

class Car:
    def __init__(self, **optional_args):
        self.make = optional_args.get("make")
        self.model = optional_args.get("model")


my_car = Car(make="Ford")
print(my_car.model)
