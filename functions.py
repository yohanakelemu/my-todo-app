# constant variable with static values
FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of
    to-dos item
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


# to avoid call from anothor module"""
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
