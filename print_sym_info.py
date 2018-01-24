# Loads a Kconfig and a .config and prints a symbol.
#
# Usage:
#
#   $ make [ARCH=<arch>] scriptconfig SCRIPT=Kconfiglib/examples/print_sym_info.py SCRIPT_ARG=<name>
#
# Example output for SCRIPT_ARG=MODULES:
#
# menuconfig MODULES
#   bool
#   prompt "Enable loadable module support"
#   option modules
#   help
#     Kernel modules are small pieces of compiled code which can
#     be inserted in the running kernel, rather than being
#     permanently built into the kernel.  You use the "modprobe"
#     tool to add (and sometimes remove) them.  If you say Y here,
#     many parts of the kernel can be built as modules (by
#     answering M instead of Y where indicated): this is most
#     useful for infrequently used options which are not required
#     for booting.  For more information, see the man pages for
#     modprobe, lsmod, modinfo, insmod and rmmod.
#     
#     If you say Y here, you will need to run "make
#     modules_install" to put the modules under /lib/modules/
#     where modprobe can find them (you may need to be root to do
#     this).
#     
#     If unsure, say Y.
# 
# value = n
# visibility = y
# currently assignable values: n, y
# defined at init/Kconfig:1674

from kconfiglib import *
import sys
import os

def set_default_value(sym):
    value = sym.user_value
    if value == None and len(sym.defaults) >= 1:
        if sym.orig_type == BOOL or sym.orig_type == TRISTATE:
            sym.set_value(expr_value(sym.defaults[0][0]) if expr_value(sym.defaults[0][1]) == 2 else 0)
            return True
        elif sym.defaults[0][1] == sym.kconfig.y and not isinstance(sym.defaults[0][0], tuple):
            sym.set_value(sym.defaults[0][0].str_value)
            return True
    return False


def indent_print_config(sym):
    print("Name = " + sym.name)
    print("Type = " + TYPE_TO_STR[sym.orig_type])

    print("currently assignable values: " +
      ", ".join([TRI_TO_STR[v] for v in sym.assignable]))

    print("Value = " + str(sym.user_value))

def set_default(node):
    changed = False
    while node:
        if isinstance(node.item, Symbol):
            changed = changed or set_default_value(node.item)

        if node.list:
            changed = changed or set_default(node.list)

        node = node.next

def set_default_until_all_set(node):
    changed = True
    while changed:
        changed = set_default(node)

def print_items(node):
    while node:
        if isinstance(node.item, Symbol):
            indent_print_config(node.item)

        if node.list:
            print_items(node.list)

        node = node.next

kconf = Kconfig(sys.argv[1])

if os.path.exists(".config"):
    print("using existing .config")
    kconf.load_config(".config")

set_default_until_all_set(kconf.top_node)
print_items(kconf.top_node)
