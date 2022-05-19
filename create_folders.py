import os
from os import path
from anytree import Node, RenderTree
from termcolor import colored

'''
Standard folder structure
author: Ursa Ursic 2021

This script creates a new folder for your project. Define the parent directory where the project will be created and 
the project name.
If you choose to create a standard folder system, set standard_form to True. 
If you want to create a custom folder structure, change standard_form to False.

If the project already exists in the parent directory, it will not be overwritten - you will get a message saying that
the project (or folder) already exists. 

Try this: 
paper
├── raw_data
│   ├── LICENSE
│   ├── README.md
│   ├── experiment1
│   │   ├── a1.tif
│   │   └── a2.tif
│   └── experiment2
│       ├── b1.tif
│       └── b2.tif
├── software
│   ├── LICENSE
│   ├── README.md
│   ├── figure1.py
│   ├── figure2
│   └── image_processing
│       ├── Fiji.app
│       └── macros
│           └── bioimage_analysis.ijm
└── text_publication
     └── draft.tex
'''


parent_directory = "/Users/ursic/Documents/PhD/Projects"
project_name = "How do cells find their center?"
standard_form = True


def standard_folder_form():
    project = Node(project_name)
    readme_file = Node("README.txt", parent=project)
    folder1 = Node("Raw data", parent=project)
    folder2 = Node("Data analysis", parent=project)
    folder3 = Node("Literature", parent=project)
    folder4 = Node("Results", parent=project)
    subfolder11 = Node("Subfolder1", parent=folder1)
    subfolder12 = Node("Subfolder2", parent=folder1)

    for pre, fill, node in RenderTree(project):
        print("%s%s" % (pre, node.name), end='')
        node_path = str(node)[6:-2]
        folder_path = parent_directory + node_path

        if path.exists(folder_path):
            print(colored(f"    Folder {node.name} already exists.", 'green'))
        elif node_path.endswith('.txt') and not path.exists(node_path):
            open(folder_path, "w+")
            print('')
        elif not path.exists(folder_path) and not node_path.endswith('.txt'):
            os.mkdir(folder_path)
            print('')


def custom_folder_form():
    '''TODO: Custom folder form - make with tkinker'''



if __name__ == "__main__":
    if standard_form:
        standard_folder_form()
    else:
        custom_folder_form()