import os
from pathlib import Path
import logging
##Logging
logging.basicConfig(Level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name = "deepClassfier"

list_file = [
    ".github/workflows/.gitkeep","""Git cannot add a completely empty directory. 
                                    People who want to track empty directories in Git have created the convention of putting files called .gitkeep in these directories. """
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/utlis/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipiline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "config/config.yaml",
    "dvx.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirments.txt",
    "requirments_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials_01.ipynb"
]

for filepath in list_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)# to seprate directory and filename
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info()


    

