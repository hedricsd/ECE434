#include <linux/build-salt.h>
#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0xc3f56f69, "module_layout" },
	{ 0xfe990052, "gpio_free" },
	{ 0xc1514a3b, "free_irq" },
	{ 0xf48c71db, "gpiod_unexport" },
	{ 0xd6b8e852, "request_threaded_irq" },
	{ 0xe3ea02ac, "gpiod_to_irq" },
	{ 0x6af8f963, "gpiod_set_debounce" },
	{ 0x6bbc18e9, "gpiod_direction_input" },
	{ 0x275d3d7c, "gpiod_export" },
	{ 0xfe4e49ad, "gpiod_direction_output_raw" },
	{ 0x47229b5c, "gpio_request" },
	{ 0xefd6cf06, "__aeabi_unwind_cpp_pr0" },
	{ 0x7c32d0f0, "printk" },
	{ 0x5138b01f, "gpiod_get_raw_value" },
	{ 0xd4e86782, "gpiod_set_raw_value" },
	{ 0xe85fa8e3, "gpio_to_desc" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";


MODULE_INFO(srcversion, "728B99D49403DB2CE4B151E");
