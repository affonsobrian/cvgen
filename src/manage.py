import argparse
import os
import re
from os import listdir
from os.path import isfile, join
from main import main


def snake_case(value):
    """
    Convert camel case to snake case.
    i.e.: CamelCase turns to camel_case
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', value).lower() 


def get_models_files(path):
    """
    Returns a list with the names of the models files
    """
    not_allowed_files = ('__init__.py', '__init__.pyc',)
    files = []
    for f in listdir(path):
        if not isfile(join(path, f)):
            continue
        if f in not_allowed_files:
            continue
        f_save_name = f.replace('.py', '')
        files.append(f_save_name)
    return files


def build_models_init(path, files):
    """
    Prepares the __init__.py from the models package
    """
    comment = '"""\nThis code was generated automatically by the Builder\n"""\n'
    with open(f'{path}/__init__.py', 'w') as open_file:
        open_file.write(comment)
        for f in files:
            open_file.write(f"from .{f} import {f}\n")
        open_file.write('\n\nvariables = {')
        last = len(files) - 1
        for index, f in enumerate(files):
            open_file.write(f"\n    '{snake_case(f)}': {f}")
            if index == last:
                continue
            open_file.write(f",")
        open_file.write("\n}")
    print('Builded with success')


parser = argparse.ArgumentParser()
optional = parser.add_argument_group("optional arguments")
optional.add_argument(
    "-b", "--build", help="build the project, so you can run it",  action="store_true")
optional.add_argument(
    "-r", "--run", help="run the project",  action="store_true")

args = parser.parse_args()

if not args:
    raise Exception("You must pass a command, type --help or -h to see")
if args.build:
    path = os.path.abspath(__file__)
    path = path.replace(__file__, 'models')
    files = get_models_files(path)  
    build_models_init(path, files)
elif args.run:
    main()

