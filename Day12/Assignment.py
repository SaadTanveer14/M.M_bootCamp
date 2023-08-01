

def get_name(arg_name):
    while arg_name == "" or arg_name.isdigit() is True:

        arg_name = input("Invalid Name Enter your Name Again ")
    return arg_name


def get_age(arg_age):
    while arg_age.isdigit() is False or arg_age == "" or int(arg_age) < 0:
        arg_age = input("Invalid Age Enter your Age Again ")
    return arg_age


def get_role(arg_role):
    while arg_role == "":
        arg_name = input("Invalid Role Enter your Role Again ")
    return arg_role


def print_details(arg_name, arg_age, arg_role):
    print(f"Name: {arg_name}, \nAge: {arg_age}, \nRole: {arg_role}")


name = get_name(input("Enter your Name "))
age = get_age(input("Enter your Age "))
role = get_role(input("Enter your Role "))

print_details(name, age, role)
