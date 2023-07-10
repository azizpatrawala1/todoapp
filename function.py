FILEPATH = "C:\pythonProject\web_app1/todos.txt"
#variuables that hpld constants are wrriten in all caps and at top of page
def get_todos(filepath=FILEPATH):
    """ reads a text file and returns the list
    pf to do items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
     with open(filepath, "w") as file:
         file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")