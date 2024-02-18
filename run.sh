#!/bin/bash

export PYTHONPATH=../py8dis/py8dis

python digiac-mac-iii.py > digiac-mac-iii.asm
beebasm -i digiac-mac-iii.asm -o digiac-mac-iii.bin
md5sum digiac-mac-iii.rom digiac-mac-iii.bin
