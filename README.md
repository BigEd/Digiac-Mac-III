# Digiac-Mac-III
Disassembly and supporting info for this 6502 trainer board

It's a work in progress. Using py8dis for an initial disassembly.

To run the disassembly and check the results against the original ROM:

env PYTHONPATH=../py8dis/py8dis python3 digiac-mac-iii.py > digiac-mac-iii.asm
../beebasm/beebasm -i digiac-mac-iii.asm -o digiac-mac-iii.beebasm.rom -v > digiac-mac-iii.lst
cmp digiac-mac-iii.rom digiac-mac-iii.beebasm.rom 
shasum digiac-mac-iii.rom digiac-mac-iii.beebasm.rom

Some resources:
http://retro.hansotten.nl/6502-sbc/emma-by-l-j-technical-systems/digiac-6502-systems/
https://www.nxp.com/docs/en/data-sheet/SCC2681.pdf
http://archive.6502.org/datasheets/mos_6522_preliminary_nov_1977.pdf

http://forum.6502.org/viewtopic.php?f=3&t=6780

https://github.com/ZornsLemma/py8dis
https://github.com/stardot/beebasm

