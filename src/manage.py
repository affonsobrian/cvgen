import argparse
import os
from os import listdir
from os.path import isfile, join
from main import main

def build_models_init():
    path = os.path.abspath(__file__)
    path = path.replace(__file__, 'models')
    not_allowed_files = ('__init__.py', '__init__.pyc',)
    files = [f for f in listdir(path) if isfile(join(path, f))]
    files = []
    for f in listdir(path):
        if not isfile(join(path, f)):
            continue
        if f in not_allowed_files:
            continue
        f_save_name = f.replace('.py', '')
        files.append(f_save_name)
    comment = '"""\nThis code was generated automatically by the Builder\n"""\n'
    with open(f'{path}/__init__.py', 'w') as open_file:
        open_file.write(comment)
        for f in files:
            open_file.write(f"from .{f} import {f}\n")

    print('Builded with success')

parser = argparse.ArgumentParser()
optional = parser.add_argument_group("optional arguments")
optional.add_argument(
    "-b", "--build", help="build the project, so you can run it",  action="store_true")
optional.add_argument(
    "-r", "--run", help="run the project",  action="store_true")


args = parser.parse_args()
print(args)

if not args:
    raise Exception("You must pass a command, type --help or -h to see")
if args.build:
    build_models_init()
elif args.run:
    main()
