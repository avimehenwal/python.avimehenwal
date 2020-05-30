# https://github.com/pydoit/doit

DOIT_CONFIG = {
    'backend': 'json',
    'dep_file': 'doit-db.json',
    'verbosity': 2,
}

def task_docs_dev():
    """vuepress dev docs"""
    cmd = 'vuepress dev docs'
    return {
        'actions': [cmd],
    }

def task_docs_build():
    """vuepress build docs"""
    cmd = 'vuepress build docs'
    return {
        'actions': [cmd],
    }

def task_update_deps():
    """Update pip requirnments.txt file"""
    cmd = 'pip freeze | tee requirements.txt'
    return {
        'actions': [cmd],
        'targets': ["requirements.txt"]
    }