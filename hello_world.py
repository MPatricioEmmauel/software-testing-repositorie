"""This module contains a simple function to greet a user based on their input."""


def greet_user(name):
    """
    Greet the user with their name.

    Parameters:
    name (str): The name of the user to greet.

    Returns:
    str: A greeting string.
    """
    return f"Hello World, {name}!"


def main():
    """
    Main function to prompt the user for their name and print a greeting.
    """
    name = input("Escribe tu Nombre: ")
    greeting = greet_user(name)
    print(greeting)


if __name__ == "__main__":
    main()
