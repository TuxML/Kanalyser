# Loads a Kconfig and a .config and prints a symbol.
#
# Usage:
#
#   $ make [ARCH=<arch>] scriptconfig SCRIPT=Kconfiglib/examples/print_sym_info.py SCRIPT_ARG=<name>
#
# Example output for SCRIPT_ARG=MODULES:
#
# menuconfig MODULES
# 	bool
# 	prompt "Enable loadable module support"
# 	option modules
# 	help
# 	  Kernel modules are small pieces of compiled code which can
# 	  be inserted in the running kernel, rather than being
# 	  permanently built into the kernel.  You use the "modprobe"
# 	  tool to add (and sometimes remove) them.  If you say Y here,
# 	  many parts of the kernel can be built as modules (by
# 	  answering M instead of Y where indicated): this is most
# 	  useful for infrequently used options which are not required
# 	  for booting.  For more information, see the man pages for
# 	  modprobe, lsmod, modinfo, insmod and rmmod.
# 	  
# 	  If you say Y here, you will need to run "make
# 	  modules_install" to put the modules under /lib/modules/
# 	  where modprobe can find them (you may need to be root to do
# 	  this).
# 	  
# 	  If unsure, say Y.
# 
# value = n
# visibility = y
# currently assignable values: n, y
# defined at init/Kconfig:1674

from kconfiglib import Kconfig, TRI_TO_STR, TYPE_TO_STR, Symbol, Choice, MENU, COMMENT
import sys

def indent_print(s, indent):
    print(" "*indent + s)

def indent_print_config(sym, indent):
	print(" "*indent + "Name = " + sym.name)
	print(" "*indent + "Type = " + TYPE_TO_STR[sym.orig_type])

	print(" "*indent + "currently assignable values: " +
      ", ".join([TRI_TO_STR[v] for v in sym.assignable]))

def print_items(node, indent):
    while node:
        if isinstance(node.item, Symbol):
            indent_print_config(node.item, indent)

        elif isinstance(node.item, Choice):
            indent_print("choice", indent)

        elif node.item == MENU:
            indent_print('menu "{}"'.format(node.prompt[0]), indent)

        elif node.item == COMMENT:
            indent_print('comment "{}"'.format(node.prompt[0]), indent)


        if node.list:
            print_items(node.list, indent + 2)

        node = node.next

kconf = Kconfig(sys.argv[1])
print_items(kconf.top_node, 0)
