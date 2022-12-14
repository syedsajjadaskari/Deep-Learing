import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name = "deepClassifier"

"""Git cannot add a completely empty directory. 
                                    People who want to track empty directories in Git have created the convention of putting files called .gitkeep in these directories. """
list_file = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",#specific fot the test
    "tests/integration/__init__.py",# for all the test
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt", #requirement of the user
    "requirements_dev.txt",#requirements of the developer
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
        logging.info(f"creating directory: {filename} for file {filename}")
    #if not exist or fil size is eual to sero then create a file
    # to not to overwrite
    if(not os.path.exists(filepath)) or (os.path.getsize) == 0: 
        with open(filepath, "w") as f:
            pass ## Create a empty file
            #store logging info mation
            logging.info(f"Creating empty file:{filedir}")

    else:
        logging.info(f"file already exist{filename}")


    

