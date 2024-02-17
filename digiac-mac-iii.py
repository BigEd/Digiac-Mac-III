# control file for py8dis
# initial disassembly of 16k ROM file from Digiac Mac-III 6502 trainer board
#
# This work (c) 2024 by BigEd and hoglet is licensed under CC BY-SA 4.0.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/

from commands import *

#config.set_hex_dump(False)
#config.set_label_references(False)
config.set_inline_comment_column(80)

# Load the program to be disassembled into the debugger's memory.
# The md5sum is optional but helps avoid confusion if there are
# multiple versions of the same program.

# take1
# load(0xc000, "digiac-mac-iii.rom", "6502", "83d9634079b0b7a116e2b425cc8dc786")

# take2
load(0xc000, "digiac-mac-iii.rom", "6502", "18c01e83131158941665ff91bbb65ea7")

entry(0xf600, "application_1");
label(0xfa00, "application_1_menu")
expr(0xf928, ">application_1_menu")

# take2 second application
entry(0xfb00, "application_2");
label(0xfe00, "application_2_menu")
expr(0xfd49, ">application_2_menu")
wordentry(0xfb98, 7);

# nonentry() prevent tracing, useful where embedded data follows JSR,
# or when a unconditional branch is followed by data.
nonentry(0xe174)

# some likely jumptable entries spotted by eye
wordentry(0xc6c5, 5);
nonentry(0xc6c5)
wordentry(0xc6d2, 5);
nonentry(0xc6d2)
wordentry(0xc6df, 5);
nonentry(0xc6df)
wordentry(0xe6f3, 8);
wordentry(0xed39, 17);
wordentry(0xed6f, 3);

# take1
# wordentry(0xf688, 8);

# take2
wordentry(0xf692, 8);

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

entry(0xc080, "abi_unknown_1")
entry(0xc084, "abi_unknown_2")
entry(0xc088, "abi_unknown_3")

# pick vectors from top of ROM
wordentry(0xfffa, 3);

# the vectors themselves
entry(0xe0dc, "nmi_handler")
entry(0xf022, "reset_handler")
entry(0xe0ca, "irq_brk_handler")

# the I/O devices: a 2681 UART and a 6522 probably
label(0x8000, "uart_reg_0")
label(0x8001, "uart_reg_1")
label(0x8002, "uart_reg_2")
label(0x8003, "uart_reg_3")
label(0x8004, "uart_reg_4")
label(0x8005, "uart_reg_5")
label(0x8006, "uart_reg_6")
label(0x8007, "uart_reg_7")
label(0x8008, "uart_reg_8")
label(0x8009, "uart_reg_9")
label(0x800a, "uart_reg_a")
label(0x800b, "uart_reg_b")
label(0x800d, "uart_reg_d_input_ports")
label(0x800e, "uart_reg_e")
label(0x800f, "uart_reg_f")

label(0x9000, "via_reg_0")
label(0x9001, "via_reg_1")
label(0x9002, "via_reg_2")
label(0x9003, "via_reg_3")
label(0x9004, "via_reg_4")
label(0x9005, "via_reg_5")
label(0x900b, "via_reg_11")
label(0x900d, "via_reg_13")
label(0x900e, "via_reg_14")

label(0xa000, "user_eprom_id_lo")
label(0xa001, "user_eprom_id_hi")
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

# some vectors appear in constants
entry(0xc8cd, "complex_irq_handler")
expr(0xc85e, "<complex_irq_handler")
expr(0xc863, ">complex_irq_handler")

# take1
# entry(0xf854, "simple_irq_handler")
# expr(0xf7fc, "<simple_irq_handler")
# expr(0xf801, ">simple_irq_handler")

# take2
entry(0xf862, "simple_irq_handler")
expr(0xf80a, "<simple_irq_handler")
expr(0xf80f, ">simple_irq_handler")

entry(0xdef6, "default_brk_handler")
expr(0xdd4a, "<default_brk_handler")
expr(0xdd4f, ">default_brk_handler")
expr(0xe733, "<default_brk_handler")
expr(0xe738, ">default_brk_handler")

entry(0xe008, "alt_nmi_handler")
expr(0xdfdd, "<alt_nmi_handler")
expr(0xdfe2, ">alt_nmi_handler")

entry(0xdd7c, "stack_underflow_handler")
# take 1
#expr(0xf163, ">stack_underflow_handler")
#expr(0xf168, "<(stack_underflow_handler-1)")
# take 2
expr(0xf17c, ">(stack_underflow_handler-1)")
expr(0xf181, "<(stack_underflow_handler-1)")

# looks like code but cannot yet see how it is reached
entry(0xc262, "maybe_unreachable_c262")
entry(0xc5e7, "maybe_unreachable_c5e7")
entry(0xe95b, "maybe_unreachable_e95b")

# some identified routines
label(0xc21f, "serial_read_char")
label(0xcb1c, "read_keypad")

# take 1
# label(0xf184, "rti_only")
# take 2
label(0xf19d, "rti_only")

# some identified tables and strings
label(0xcb54, "keypad_keys")

# data tables
byte(0xc765, 8)
label(0xc765, "uart_reg_1_initial")
byte(0xc76d, 6)
label(0xc76d, "uart_reg_4_initial")
byte(0xc773, 2)
label(0xc773, "uart_reg_0_initial")

# disassembler data tables
byte(0xe555, 0x69)

# other data tables
byte(0xedb7, 0x62)

# printable strings

# Handle blocks of code like
#    lda #&05
#    sta l0007
#    lda #&c3
#    sta l0008

def string_ref(addr, friendly):
    string_addr = get_u8_binary(addr + 1) + 256 *  get_u8_binary(addr + 5)
    string_label = "string_" + friendly
    label(string_addr, string_label)
    expr(addr + 1, "<" + string_label)
    expr(addr + 5, ">" + string_label)

string_ref(0xc2a4, "mac")
string_ref(0xc5e7, "done")
string_ref(0xc630, "error")
string_ref(0xccf6, "memory_limit")
string_ref(0xcd8a, "a_x_y_pc_sp_sr")
string_ref(0xcf18, "loading")
string_ref(0xcfd1, "loaded")
string_ref(0xd0aa, "device")
string_ref(0xd0e6, "start_tape")
string_ref(0xd0fb, "loading")
string_ref(0xd144, "loaded")
string_ref(0xd18e, "start_recording")
string_ref(0xd1a3, "saving")
string_ref(0xd1e3, "saved")
string_ref(0xd2b7, "calling_keypad_display_monitor")
string_ref(0xd30d, "help_commands_short")
string_ref(0xd318, "help_commands_long")
string_ref(0xd323, "press_return_for_system_address_info")
string_ref(0xd340, "help_system_addresses")
string_ref(0xdf3c, "at_breakpoint")
string_ref(0xd23e, "serial_params")
string_ref(0xe977, "load_t1_t2_cas")
string_ref(0xf16a, "lj_systems_banner")
#string_ref(0x, "")

label(0xce4e, "string_flags")

# Use all the information provided to actually disassemble the program.
go()
