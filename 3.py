import os
import shutil


def safe_mkdir(dirname):
    try:
        os.mkdir(dirname)
    except FileExistsError:
        return False
    return True


def recursive_scan(root_dir=''):
    files = {}
    for fo in os.listdir(root_dir):
        fo_abs = f'{root_dir}/{fo}'
        if os.path.isdir(fo_abs):
            files.update(recursive_scan(fo_abs))
        elif os.path.isfile(fo_abs) and fo.endswith('.html'):
            if not root_dir in files.keys():
                files[root_dir] = []
            files[root_dir].append(fo)
    return files


def pull_templates(start_dir=''):
    scan = recursive_scan(start_dir)
    templates_path = f'{start_dir}/templates'
    safe_mkdir(templates_path)
    for k, v in scan.items():
        directory = k.split('/')[-1]
        safe_mkdir(f'{templates_path}/{directory}')
        for file in v:
            try:
                shutil.copy(f'{k}/{file}', f'{templates_path}/{directory}/{file}')
            except shutil.SameFileError:
                pass


pull_templates('my_project')
