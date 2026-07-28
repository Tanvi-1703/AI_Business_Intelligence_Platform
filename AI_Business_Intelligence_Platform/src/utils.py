import os

def create_folder(path):

    if not os.path.exists(path):

        os.makedirs(path)


def print_line():

    print("=" * 70)


def print_title(title):

    print_line()

    print(title)

    print_line()