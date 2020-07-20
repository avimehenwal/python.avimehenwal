---
title: Virtual Environment
tags:
- virtual
- environment
- venv
- setup
---

# Virtual Environment

<TagLinks />

* Run multiple python appications running on different versions on same machine
* sets up relative paths (symlinks) to new interpreter

```
venv/
|-- bin
|-- include
|-- lib
|   `-- python3.8
|       `-- site-packages
|           |-- PyPI package 1
|           |-- PyPI package 2
|           |-- PyPI package N
|-- lib64 -> lib
`-- share
    `-- python-wheels
```

Python package build command

```
python setup.py --help-commands

# link source files in sites-package
python setup.py --verbose develop

# develop
Location: .../robotframework/src
# install
Location: .../robotframework/venv/lib/python3.8/site-packages
```

```mermaid
graph LR
A((Distributions)):::orange
B([Source distribution tarball]):::green
C([Binary distribution]):::purple
D[C API Extension]:::yellow
E[only C libraries]:::blue

A == sdist ==> B
A -- bdist --> C
A -- build_ext --> D
A -- build_clib --> E

subgraph Full_Package_Bundeling
    B
    C
end
subgraph Partial_Bundeling
    D
    E
end

classDef green fill:#1f9,stroke-width:0px;
classDef orange fill:#f96,stroke-width:0px;
classDef blue fill:#4B8BBE,stroke-width:0px;
classDef purple fill:#f9f,stroke:#333,stroke-width:0px;
classDef yellow fill:#FFE873,stroke-width:0px;

click A "https://stackoverflow.com/questions/1471994/what-is-setup-py" "What is setup.py"
click B "https://docs.python.org/3.8/distutils/index.html" "Distributing Python Modules (Legacy version)"
click Partial_Bundeling "https://docs.python.org/3.8/distutils/index.html" "Distributing Python Modules (Legacy version)"
```

setup.py keys | what does it do?
:-------------|--------------
`packages = ['foo']` | you are promising that the Distutils will find a file `foo/__init__.py`
`package_dir = {'foo': 'lib'}`   | inside `lib` you will find a `foo/__init__.py`
`package_data`  | might contain documentation files for package
`entry_points = {'console_scripts': ['robot = robot.run:run_cli']`  | run as a CLI tool


<Footer />
