#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import shutil
import subprocess
from time import *

def render(parts = None):
    stl_dir = "stls"
    render_dir = "render"

    if os.path.isdir(render_dir):
        if not parts:
            shutil.rmtree(render_dir)   #if doing them all clear the directory first
            sleep(0.1)
            os.makedirs(render_dir)
    else:
        os.makedirs(render_dir)

    #
    # List of individual part files
    #
    if parts:
        stls = [i[:-4] for i in parts]
    else:
        stls = [i[:-4] for i in os.listdir(stl_dir) if i[-4:] == ".stl"]
        #
        # Add the multipart files
        #
        for i in  os.listdir(stl_dir + os.sep + "printed"):
            if i[-4:] == ".stl" and not i[:-4] in stls:
                stls.append("printed" + os.sep + i[:-4])

    for i in stls:
        command = ['blender', 
                   '-b', "utils%srender.blend" % os.sep,
                   '-P', "utils%sviz.py" % os.sep, 
                   '--', 
                   stl_dir + os.sep + i + '.stl',
                   render_dir + os.sep + i + '.png'
                  ]
        print(' '.join(command))
        subprocess.check_output(command)

if __name__ == '__main__':
    if len(sys.argv) > 0:
        render(sys.argv[1:])
    else:
        print("usage: render [part.stl ...]")
        sys.exit(1)
