# control file for py8dis
# initial disassembly of 16k ROM file from Digiac Mac-III 6502 trainer board
#
# This work © 2024 by BigEd is licensed under CC BY-SA 4.0.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/

from commands import *

# Load the program to be disassembled into the debugger's memory.
# The md5sum is optional but helps avoid confusion if there are
# multiple versions of the same program.
load(0xc000, "digiac-mac-iii.rom.trunc", "6502", "5c5bee1f61aeaf6a387da6112720ab5b")

# some likely jumptable entries spotted by eye
wordentry(0xc6c5, 5);
wordentry(0xc6d2, 5);
wordentry(0xc6df, 5);
wordentry(0xe6f3, 8);
wordentry(0xed39, 17);
wordentry(0xed6f, 3);
wordentry(0xf688, 8);

# this is the ABI
entry(0xc000, "abi_read")
entry(0xc004, "abi_readln")
entry(0xc008, "abi_write")
entry(0xc00c, "abi_writln")
entry(0xc010, "abi_exit")
entry(0xc014, "abi_perr")

entry(0xc020, "abi_ahexto")
entry(0xc024, "abi_adecto")
entry(0xc028, "abi_toahex")
entry(0xc02c, "abi_toadec")

entry(0xc040, "abi_rdchar")
entry(0xc044, "abi_rdbyte")
entry(0xc048, "abi_wrchar")
entry(0xc04c, "abi_wrbyte")
entry(0xc050, "abi_getin")
entry(0xc054, "abi_wt1ms")
entry(0xc058, "abi_wtnms")
entry(0xc05c, "abi_crlf")
entry(0xc060, "abi_clrscr")
entry(0xc064, "abi_ledon")
entry(0xc068, "abi_ledoff")

entry(0xc080, "abi_")
entry(0xc084, "abi_")
entry(0xc088, "abi_")

# can pick vectors from top of ROM (just two because we had to truncate it)
wordentry(0xfffa, 2);

# the vectors themselves
entry(0xf022, "nmi_handler")
entry(0xe0ca, "reset_handler")
entry(0xe0dc, "irq_brk_handler")

# the I/O devices: a 2681 UART and a 6522 probably
label(0x8000, "uart_reg_0")
label(0x8001, "uart_reg_1")
label(0x8002, "uart_reg_2")
label(0x8003, "uart_reg_3")
label(0x8004, "uart_reg_4")
label(0x8008, "uart_reg_8")
label(0x8009, "uart_reg_9")
label(0x800a, "uart_reg_a")
label(0x800b, "uart_reg_b")
label(0x800d, "uart_reg_13")
label(0x800e, "uart_reg_14")
label(0x800f, "uart_reg_15")

label(0x9000, "via_reg_0")
label(0x9001, "via_reg_1")
label(0x9002, "via_reg_2")
label(0x9003, "via_reg_3")
label(0x9004, "via_reg_4")
label(0x9005, "via_reg_5")
label(0x900b, "via_reg_11")
label(0x900d, "via_reg_13")
label(0x900e, "via_reg_14")

label(0xa000, "user_eprom_sig_lo")
label(0xa001, "user_eprom_sig_hi")
label(0xa002, "user_eprom_entry")

# documented zero page
label(0x0000, "ptr")
label(0x0001, "ptr_high")
label(0x0002, "number")
label(0x0003, "number_high")

# documented memory locations
label(0x0200, "nmi_v")
label(0x0201, "nmi_v_high")
label(0x0202, "irq_v")
label(0x0203, "irq_v_high")
label(0x0204, "brk_v")
label(0x0205, "brk_v_high")
label(0x0206, "autorun_flag")

# looks like code but cannot yet see how it is reached
entry(0xc262, "maybe_unreachable_c262")
entry(0xc5e7, "maybe_unreachable_c5e7")
entry(0xdd7c, "maybe_unreachable_dd7c")
entry(0xdfd9, "maybe_unreachable_dfd9")
entry(0xe008, "maybe_unreachable_e008")
entry(0xe95b, "maybe_unreachable_e95b")

entry(0xc8cc, "maybe_unreachable_c8cc")


# some identified routines
label(0xc21f, "serial_read_char")

# Use all the information provided to actually disassemble the program.
go()
