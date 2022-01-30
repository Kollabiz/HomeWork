import os
import yaml


def safe_mkdir(dirname):        # Creates directory safely
    try:
        os.mkdir(dirname)
    except FileExistsError:
        return False        # Returns False if directory wasn't created
    return True        # Returns True if directory was created


def load_yaml(filename):        # Loads yaml file
    with open(filename, 'r') as fl:
        cnf = yaml.load(fl, yaml.Loader)
    return cnf


def mk_tree_from_dict(tree:dict, start_path=''):        # Recursively creates files from given dictionary
    for k, v in tree.items():       # For every folder (or file) in tree
        if isinstance(v, dict):        # If contents of folder is dictionary, does recursion step
            safe_mkdir(f'{start_path}{k}')
            mk_tree_from_dict(v, f'{start_path}{k}/')
        elif v == 'file':       # Else if it's a file, creates it
            with open(f'{start_path}/{k}', 'w') as fl:
                pass
        elif v == 'empty':      # Else if it's empty, just creates it
            safe_mkdir(f'{start_path}/{k}')
        else:       # Else creates both as folders
            safe_mkdir(f'{start_path}/{k}')
            safe_mkdir(f'{start_path}/{k}/{v}')


config = load_yaml('config.yml')
mk_tree_from_dict(config['Files'])
