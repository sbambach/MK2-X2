#!/bin/bash

if [ "x${PATH_TO_BLENDER}" == "x" ]; then
	PATH_TO_BLENDER="/Applications/blender.app/Contents/MacOS"
fi

export PATH="${PATH}:${PATH_TO_BLENDER}"

python render.py "$@"

