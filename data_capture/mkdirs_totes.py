# Creates directories for the CV2 "tote" data collection
# with the hierarchy [ Layout > Lighting > Views ].
# Output structure:
#       data_totes/
#           ├── layout_a
#           │   ├── light_ambient
#           │   │   ├── view_side
#           │   │   └── view_top
#           │   ├── light_side
#           │   │   ├── view_side
#           │   │   └── view_top
#           │   └── light_top
#           │       ├── view_side
#           │       └── view_top
#           ├── layout_b
#           │   ├── light_ambient
#           │   │   ├── view_side
#           │   │   └── view_top
#           │   ├── light_side
#           │   │   ├── view_side
#           │   │   └── view_top
#           │   └── light_top
#           │       ├── view_side
#           │       └── view_top
#           └── layout_c
#               ├── light_ambient
#               │   ├── view_side
#               │   └── view_top
#               ├── light_side
#               │   ├── view_side
#               │   └── view_top
#               └── light_top
#                   ├── view_side
#                   └── view_top

import os
import itertools

BASE_PATH = 'data_totes'


def create_dirs():

    dirs = {
        'layouts': [
            'layout_a',
            'layout_b',
            'layout_c',
        ],
        'lights': [
            'light_ambient',
            'light_top',
            'light_side',
        ],
        'views': [
            'view_top',
            'view_side',
        ],
    }

    paths = list(itertools.product(dirs['layouts'], dirs['lights'], dirs['views']))
    paths = [ os.path.join(*p) for p in paths ]

    for p in paths:

        path = os.path.join(BASE_PATH, p)
        print("Creating {}".format(path))
        os.makedirs(path, exist_ok=True)


create_dirs()
